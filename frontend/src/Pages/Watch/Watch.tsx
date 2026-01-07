import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"

const Watch = () => {
  const {id, episode} = useParams()
  const [episodeUrl, setEpisodeUrl] = useState('')

  useEffect(() => {
    const getData = async () => {
      let response = await fetch(`${import.meta.env.VITE_BACK_END_URL}/watch/?id=${id}`)
      let json = await response.json()
      response = await fetch(json[0])
      json = await response.json()
      setEpisodeUrl(json.links[0].link)
    }
    getData()
  }, [])


  return (
    <div>
      <video src={episodeUrl} controls={true}></video>
    </div>
  )
}

export default Watch