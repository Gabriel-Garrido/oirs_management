import {
    GET_CITIZENREQUESTS_SUCCESS,
    GET_CITIZENREQUESTS_FAIL
} from '../actions/citizenRequests/types'

const initialState = {
    citizenRequests: []
}

export default function citizenRequests(state=initialState, action) {
    const { type, payload } = action

    switch(type){
        case GET_CITIZENREQUESTS_SUCCESS:
            return {
                ...state,
                citizenRequests: payload
            }
        case GET_CITIZENREQUESTS_FAIL:
            return {
                ...state,
                citizenRequests: null
            }
        default:
            return state
    }
}
