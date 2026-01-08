import { useEffect } from "react"

const SavedLogins = () => {
  
  useEffect(() => {
    const testReponse = async () => {
      const response = await fetch('http://127.0.0.1:8000/api/saved_logins/' ,{credentials: "include"})
    }
    testReponse()
  }, [])
  return (
    <div>SavedLogins</div>
  )
}

export default SavedLogins