import { RingLoader } from "react-spinners";

function LoadingIcon () {
    return(
        <div className="flex justify-center h-screen">
            <RingLoader size={70} color={"#36D7B7"} />
          </div>
    )
}

export default LoadingIcon