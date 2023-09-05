import Head from 'next/head';
import Clock from '../components/Clock';

const cities = [
    {city: 'New York', timezone: 'America/New_York'},
    {city: 'London', timezone: 'Europe/London'},
    {city: 'Tokyo', timezone: 'Asia/Tokyo'},
    {city: 'Moscow', timezone: 'Europe/Moscow'},
];

export default function Home() {
    return (
        <div>
            <Head>
                <title>World Time App</title>
            </Head>

            <main>
                <h1>World Time App</h1>
                <div className="world-clocks">
                    {cities.map((cityData, index) => (
                        <Clock
                            key={index}
                            city={cityData.city}
                            timezone={cityData.timezone}
                        />
                    ))}
                </div>
            </main>
        </div>
    );
}
