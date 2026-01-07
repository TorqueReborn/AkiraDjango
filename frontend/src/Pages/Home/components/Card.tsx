interface CardProps {
  name: string,
  thumbnail: string
}

const Card = ({ name, thumbnail }: CardProps) => {
  return (
    <div className="w-48 shrink-0">
      <div className="line-clamp-1 text-center">
        <img src={thumbnail} className="w-48 h-72" />
        {name}
      </div>
    </div>
  )
}

export default Card