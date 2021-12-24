import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp";
import FooterComp from "../components/FooterComp";
import getObjects from "../modules/GetObjects.js";


function ListPage() {

    const [rasesList, setRasesList] = useState([])
    const [rasesNames, setRasesNames] = useState([])

    const handleObjectsList = async () => {
        const names = []
        const rasess = await getObjects()
        for (let rase of rases) {
            names.push(rase['name']);
        }
        setRasesList(rases)
        setrasesNames(names)
    }

    useEffect(()=>{
        handleObjectsList()
    }, [])

    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>Список объектов таблицы Creat</h2>
            <ul>
                {rasesNames.map((name)=>{
                    return (
                        <li key={name}>
                            <Link to={{pathname: "/list/object", data: rasesList.find(o => o.name == name)}}>{name}</Link>
                        </li>
                    )
                })}
            </ul>
            <FooterComp></FooterComp>
        </div>
    );
}

export default ListPage;
