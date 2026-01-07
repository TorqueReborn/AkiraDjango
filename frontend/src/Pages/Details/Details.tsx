import { useEffect } from 'react'
import { useParams } from 'react-router-dom'

const Details = () => {
  const {id} = useParams()
  useEffect(() => {
    const getDetails = async () => {
      const response = await fetch(`${import.meta.env.VITE_BACK_END_URL}/details/?id=${id}`)
    }
    getDetails()
  }, [])
  
  return (
    <div>
      
    </div>
  )
}

export default Details