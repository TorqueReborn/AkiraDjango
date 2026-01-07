import { useEffect, useState } from "react"
import Banner from "./components/Banner"

interface Anime {
    _id: string,
    name: string,
    banner: string
}

const Spotlight = () => {
    const [index, setIndex] = useState(0)
    const [banners, setBanners] = useState<Anime[]>()

    useEffect(() => {
        const getData = async () => {
            const response = await fetch(`${import.meta.env.VITE_BACK_END_URL}/trending`)
            const json = await response.json()
            setBanners(json.map((j: Anime) => j))
        }
        getData()
    }, [])

    useEffect(() => {
        if (banners && banners.length > 0) {
            const intervalId = setInterval(() => {
                setIndex(prevIndex => (prevIndex + 1) % banners.length)
            }, 3000)
            return () => clearInterval(intervalId)
        }
    }, [banners])

    return (
        <div>
            {banners && <Banner id={banners[index]._id} name={banners[index].name} banner={banners[index].banner} />}
        </div>
    )
}

export default Spotlight