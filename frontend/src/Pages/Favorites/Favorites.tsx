import { useEffect, useState } from "react"

const Favorites = () => {
  const [data, setData] = useState()

  useEffect(() => {
    const getData = async () => {
      const response = await fetch('http://127.0.0.1:8000/favorites/', { credentials: "include" })
      const json = await response.json()
      setData(json)
    }
    getData()
  }, [])

  return (
    <>
      <div>Favorites</div>
      {data && data.map(d => (
        <div>
          {d.animeName}
        </div>
      ))}
    </>
  )
}

export default Favorites