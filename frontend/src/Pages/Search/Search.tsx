import { useState } from "react"
import Card from "../Home/components/Card";

const Search = () => {
  const [data, setData] = useState()
  const [query, setQuery] = useState<string>('')

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  }

  const search = async () => {
    const response = await fetch(`${import.meta.env.VITE_BACK_END_URL}/search/?query=${query}`);
    const data = await response.json();
    setData(data);
  }

  return (
    <div>
      <input type="text" onChange={handleChange} />
      <button onClick={search}>Search</button>
      <div>
        {data && (
          data.map(d => (
            <Card name={d.name} thumbnail={d.thumbnail}/>
          ))
        )}
      </div>
    </div>
  )
}

export default Search