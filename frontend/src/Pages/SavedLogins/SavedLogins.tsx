import { useEffect, useState } from "react"

const SavedLogins = () => {
  const [data, setData] = useState()
  
  useEffect(() => {
    const testReponse = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/saved_logins/' ,{credentials: "include"})
      const json = await response.json()
      setData(json.logins)
    }
    testReponse()
  }, [])
  return (
    <>
      <div>SavedLogins</div>
      { data && (
        data.map(d => (
          <div>
            {d.user} - {d.os} - {d.created_at}
          </div>
        ))
      )}
    </>
  )
}

export default SavedLogins