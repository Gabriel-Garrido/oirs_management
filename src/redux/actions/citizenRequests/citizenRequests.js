import axios from 'axios'
import {
    GET_CITIZENREQUESTS_SUCCESS,
    GET_CITIZENREQUESTS_FAIL
} from './types'

export const get_citizenRequests = () => async dispatch => {
    const config = {
        headers: {
            'Accept': 'application/json'
        }
    }
    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/citizenRequests/solicitudes/`, config)
        
        if(res.status === 200) {
            dispatch({
                type: GET_CITIZENREQUESTS_SUCCESS,
                payload: res.data
            })
        } else {
            dispatch({
                type: GET_CITIZENREQUESTS_FAIL
            })
        }
    } catch(err) {
        dispatch({
            type: GET_CITIZENREQUESTS_FAIL
        })
    }
}
