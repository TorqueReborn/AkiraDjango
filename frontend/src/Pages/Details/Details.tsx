import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

interface AnimeData {
    id: string,
    name: string,
    englishName: string,
    thumbnail: string,
    description: string,
}

const Details = () => {
  const {id} = useParams()
  const [animeData, setAnimeData] = useState<AnimeData>()

  useEffect(() => {
    const getDetails = async () => {
      const response = await fetch(`${import.meta.env.VITE_BACK_END_URL}/details/?id=${id}`)
      const json = await response.json()
      setAnimeData(json)
    }
    getDetails()
  }, [])
  
  return (
    <div>
      {animeData && (<div>
        <img src={animeData.thumbnail}/>
        {animeData.englishName} <br/>
        {animeData.description}
      </div>)}
    </div>
  )
}

export default Details