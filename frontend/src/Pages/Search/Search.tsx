import { useState } from "react"

const Search = () => {
  const [query, setQuery] = useState<string>('')

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  }

  const search = async () => {
    console.log(query)
  }

  return (
    <div>
      <input type="text" onChange={handleChange}/>
      <button onClick={search}>Search</button>
    </div>
  )
}

export default Search