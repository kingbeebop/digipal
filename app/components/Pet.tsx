import React from "react";

const Pet: React.FC = () => {
    
    return (
        <div>
            <h1>Digipal</h1>
            {/* Render pet sprites: */}
            <div id='digipal-render'>
                <div id='pet-container'></div>
            </div>
            <div id='actions'></div>
            <button className="actions action-greet" id='action-greet'>Greet pal</button> 
            <button className="actions action-feed" id='action-feed'>Feed pal</button> 
            {/* You can use your Button component here */}
        </div>
    );
  
};


export default Pet;