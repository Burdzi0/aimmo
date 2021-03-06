import { switchMap, mapTo, zip, take, tap, map } from 'rxjs/operators'

import actions from './actions'
import types from './types'
import { ofType } from 'redux-observable'
import { gameTypes } from '../Game'
import { editorTypes } from '../Editor'

const initializePyodideEpic = (action$, state$, { pyodideRunner: { initializePyodide } }) =>
  action$.pipe(
    ofType(gameTypes.SOCKET_CONNECT_TO_GAME_REQUEST),
    switchMap(initializePyodide),
    mapTo(actions.pyodideInitialized())
  )

const initialUpdateAvatarCodeEpic = (action$, state$, { pyodideRunner: { updateAvatarCode } }) =>
  action$.pipe(
    zip(
      action$.pipe(ofType(types.PYODIDE_INITIALIZED), take(1)),
      action$.pipe(ofType(editorTypes.GET_CODE_SUCCESS), take(1))
    ),
    switchMap(() => updateAvatarCode(state$.value.editor.code.codeOnServer)),
    map(actions.avatarCodeUpdated)
  )

const updateAvatarCodeEpic = (action$, state$, { pyodideRunner: { updateAvatarCode } }) =>
  action$.pipe(
    ofType(editorTypes.POST_CODE_SUCCESS),
    switchMap(() =>
      updateAvatarCode(state$.value.editor.code.codeOnServer, state$.value.game.gameState.turnCount)
    ),
    map(actions.avatarCodeUpdated)
  )

const computeNextActionEpic = (
  action$,
  state$,
  { api: { socket }, pyodideRunner: { computeNextAction$ } }
) =>
  action$.pipe(
    ofType(types.PYODIDE_INITIALIZED),
    switchMap(() =>
      action$.pipe(
        ofType(gameTypes.SOCKET_GAME_STATE_RECEIVED),
        switchMap(({ payload: { gameState } }) =>
          computeNextAction$(
            gameState,
            gameState.players.find(
              player => player.id === state$.value.game.connectionParameters.currentAvatarID
            )
          )
        ),
        tap(socket.emitAction),
        map(actions.avatarsNextActionComputed)
      )
    )
  )

export default {
  initializePyodideEpic,
  initialUpdateAvatarCodeEpic,
  updateAvatarCodeEpic,
  computeNextActionEpic
}
