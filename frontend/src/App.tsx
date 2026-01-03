import { useEffect } from "react"

const App = () => {
  useEffect(() => {
    const getResponse = async () => {
      const response = await fetch('http://127.0.0.1:8000/test/')
      console.log(response)
    }
    getResponse()
  }, [])

  return (
    <div className="bg-black text-white">App</div>
  )
}

export default App