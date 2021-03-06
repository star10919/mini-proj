import React,{useEffect, useState} from 'react'
import 'member/styles/MemberDetail.css'

const MemberDetailComponent = () => {
    const [member, SetMember] = useState({})


    useEffect(() => {  // return 보다 먼저 작동하게 하려고 useEffect 사용하는 것임
      SetMember(JSON.parse(localStorage.getItem("selectedMember")))   //parse : 시리얼라이저 돼있는것을 JSON으로 복구
    }, {})  //getItem 은 키
 
        
    return (<>
      <div className="member-detail-card">
        <h2 style={{"text-align":"center"}}>회원 정보</h2>
        <img src="https://www.w3schools.com/w3images/team2.jpg"  style={{"width":"100%"}}/>
        <h1>{member.name}</h1>
            <p className="member-detail-title">CEO & Founder, Example</p>
            <p>Harvard University</p>
            <div style={{"margin": "24px 0"}}>
              <a className="member-detail-a" href="#"><i className="fa fa-dribbble"></i></a> 
              <a className="member-detail-a" href="#"><i className="fa fa-twitter"></i></a>  
              <a className="member-detail-a" href="#"><i className="fa fa-linkedin"></i></a>  
              <a className="member-detail-a" href="#"><i className="fa fa-facebook"></i></a> 
            </div>
            <p><button className="member-detail-button">Contact</button></p>
        </div>
         

</>)
}
export default MemberDetailComponent