"use client"

import React, {useEffect, useState} from 'react';

function Clock({city, timezone}) {
    const [time, setTime] = useState('');
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const calculateTime = () => {
            const now = new Date();
            const cityTime = new Date(
                now.toLocaleString('en-US', {timeZone: timezone})
            );

            const timeString = cityTime.toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
            });

            setTime(timeString);
            setLoading(false);
        };

        calculateTime();
        const intervalId = setInterval(calculateTime, 1000);

        return () => clearInterval(intervalId);
    }, [timezone]);

    return (
        <div className="world-clock">
            <h2>{city}</h2>
            {loading ? <p>Loading...</p> : <p>{time}</p>}
        </div>
    );
}

export default Clock;
