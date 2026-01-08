import { useEffect } from "react"

const SavedLogins = () => {
  
  useEffect(() => {
    const testReponse = async () => {
      const response = await fetch('www.google.com' ,{credentials: "include"})
    }
  }, [])
  return (
    <div>SavedLogins</div>
  )
}

export default SavedLogins