import React,{useEffect, useState} from 'react'
import 'member/styles/MemberDetail.css'
import { memberDelete } from 'api'
const MemberDeleteForm = () => {
    const [password, setPassword] = useState({})


    const handleSubmit = e => {
      e.preventDefault()
      const member = JSON.parse(localStorage.getItem("loginedMember"))
      alert(password)
      member.password = password
      alert(JSON.stringify(member))
      
      memberDelete({member})
      .then(res => {
        alert(`탈퇴 완료 : ${res.data.result} `)
        // history.push('login')
        
      })
      .catch(err => {
        alert(`탈퇴 실패 : ${err} `)
  
      })
    }

    return (<>
    <form method="put" onSubmit={handleSubmit} >
            
                <h2 style={{"text-align":"center"}}>회원탈퇴</h2>
        <div className="container">
          <label labelFor="password"><b>비밀번호 </b></label>
          <input type="password" placeholder="Enter Password" onChange={e => {setPassword(e.target.value)}} name="password" required/>
              
          <button type="submit">확 인</button>
         
        </div>

      </form>

       
      </>)
}

export default MemberDeleteForm