import Button from "./components/Button"
import { useNavigate } from "react-router-dom"

const Nav = () => {
  const navigate = useNavigate()

  const handleClick = () => {
    navigate(`/saved-logins`)
  }

  const handleFavorites = () => {
    navigate(`/favorites`)
  }

  return (
    <div className="flex items-center relative h-16">
      <div className="absolute right-10">
        <Button />
      </div>
      <button onClick={handleClick}>Saved Logins</button>
      <button onClick={handleFavorites}>Favorites</button>
    </div>
  )
}

export default Nav