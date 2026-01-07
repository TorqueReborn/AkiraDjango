import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'

interface AvailableEpisodesDetail {
  sub: string[]
  dub: string[]
  raw: string[]
}

interface AnimeData {
  id: string
  name: string
  thumbnail: string
  englishName: string
  description: string
  availableEpisodesDetail: AvailableEpisodesDetail
}

const Details = () => {
  const {id} = useParams()
  const [animeData, setAnimeData] = useState<AnimeData>()
  const navigate = useNavigate()

  const handleClick = (episode: string) => {
    navigate(`/watch/${id}/${episode}`)
  }

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
        {animeData.description} <br />
        sub: {animeData.availableEpisodesDetail.sub.map((data) => (<button className='bg-white text-black p-4' onClick={() => handleClick(data)}>{data}</button>))} <br />
        dub: {animeData.availableEpisodesDetail.dub.map((data) => (<button className='bg-white text-black p-4' onClick={() => handleClick(data)}>{data}</button>))} <br />
        raw: {animeData.availableEpisodesDetail.raw.map((data) => (<button className='bg-white text-black p-4' onClick={() => handleClick(data)}>{data}</button>))} <br />
      </div>)}
    </div>
  )
}

export default Details