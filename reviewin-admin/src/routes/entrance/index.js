import { h } from 'preact';
import { route } from 'preact-router';
import style from './style.css';

const Entrance = () => {
    
    if (window.rvwnClient.token) {
        window.rvwnClient.getSession()
        .then((session) => {
            if (session.user.role == "partner") {
                route("/products", true)
            }
            else {
                route("/settings", true)
            }
        })
        .catch((err) => {
            if (err) { alert(err) }
            // and log out
        })
    }
    else {
        route("/login", true)
    }

    return (
        <div>
            <p>Loading...</p>
        </div>
    )
};

export default Entrance;
