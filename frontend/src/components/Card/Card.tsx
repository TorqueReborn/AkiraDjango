import React from "react";

type CardProps = {
    name: string;
    thumbnail: string;
}

const Card: React.FC<CardProps> = ({ name, thumbnail }) => {
    return (
        <div className="bg-black text-white">
            <img src={thumbnail} />
            { name }
        </div>
    );
}

export default Card;