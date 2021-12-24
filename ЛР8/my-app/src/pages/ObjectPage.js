import { Link } from "react-router-dom";
import HeaderComp from "../components/HeaderComp";
import FooterComp from "../components/FooterComp";


function ObjectPage(params) {
    const rasesList = params.location.data
    return (
        <div>
            <HeaderComp></HeaderComp>
            <h2>{rasesList.name}</h2>
            <h4>Описание :</h4>
            <p>{rasesList.discription}</p>
        
            <Link to="/list"><button>Назад</button></Link>
            <FooterComp></FooterComp>
        </div>
    );
}

export default ObjectPage;
