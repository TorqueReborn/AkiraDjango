import { useNavigate } from "react-router-dom"

interface CardProps {
  id: string,
  name: string,
  thumbnail: string
}

const Card = ({ id, name, thumbnail }: CardProps) => {
  const navigate = useNavigate()

  const handleClick = () => {
    navigate(`/${id}`)
  }

  return (
    <div className="w-52 relative ml-8 flex-none" onClick={handleClick}>
      {<img src={thumbnail} alt={name} className="h-72" />}
      <div className="absolute -bottom-3 -left-3 origin-left -rotate-90 line-clamp-1">
        {name}
      </div>
    </div>
  )
}

export default Card