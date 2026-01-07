import { useEffect, useState } from "react";
import Card from "../components/Card/Card";

interface Show {
    _id: string;
    name: string;
    englishName: string | null;
    thumbnail: string;
}

const Home = () => {
    const [shows, setShows] = useState<Show[]>([]);

    useEffect(() => {
        const getRecentAnime = async () => {
            const response = await fetch('http://127.0.0.1:8000/')
            const json = await response.json()
            setShows(json)
        }
        getRecentAnime()
    }, [])

    return <div>
            { shows.map(show => (
                <Card name={show.name} thumbnail={show.thumbnail}/>
                )) }
        </div>
}

export default Home;