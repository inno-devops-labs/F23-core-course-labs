fetch('/api/time/now')
    .then(res => res.json())
    .then(res => {
        let date = new Date(Date.parse(res.timestamp));
        document.getElementById("time").innerText = date.toLocaleString("ru-ru");
    })
