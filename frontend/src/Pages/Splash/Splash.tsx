import { MdKeyboardArrowRight } from "react-icons/md";

const Splash = () => {

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div className="flex items-center gap-4">
        <img src="/logo.png" width={100} />
        <div className="text-6xl mt-3 ml-4 font-bold bg-linear-to-r from-indigo-800 via-blue-400 to-purple-400 text-transparent bg-clip-text">
          Akira
        </div>
      </div>
      <div className="mt-36 rounded-full bg-white cursor-pointer" tabIndex={0}>
        <MdKeyboardArrowRight size={45} className="text-black" />
      </div>
    </div>
  )
}

export default Splash