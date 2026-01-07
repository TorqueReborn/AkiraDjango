import { useNavigate } from "react-router-dom"

interface BannerProps {
    id: string,
    name: string,
    banner: string
}

const Banner = ({ id, name, banner }: BannerProps) => {
    const navigate = useNavigate()

    const handleClick = () => {
        navigate(`/${id}`)
    }
    return (
        <div className="h-72 relative" onClick={handleClick}>
            <h2 className="absolute bottom-10 left-10 text-2xl font-black right-10">{name}</h2>
            <img className="h-full w-full object-cover" src={banner} alt="Anime Banner" />
        </div>
    )
}

export default Banner