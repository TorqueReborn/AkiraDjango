import { useNavigate } from "react-router-dom"

const Button = () => {
  const navigate = useNavigate()

  const handleClick = () => {
    navigate(`/login`)
  }
  
  return (
    <div onClick={handleClick} className='text-xl text-bold bg-gray-500 px-3 py-1 rounded-2xl hover:bg-amber-50 hover:text-black cursor-pointer'>
        Login
    </div>
  )
}

export default Button