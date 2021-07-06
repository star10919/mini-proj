import React,{useEffect, useState} from 'react'
import 'member/styles/MemberModify.css'
import { memberList, memberModify } from 'api'
import { useHistory } from 'react-router'

const MemberModifyForm = () => {
    const [changedPassword, setChangedPassword] = useState('')
    const history = useHistory()


    const handleSubmit = e => {
      e.preventDefault()
      if(localStorage.getItem("loginedMember") == null){  //null 값 체크
        console.log('localStorage.getItem is null')
      }else{
        console.log('localStorage.getItem is not null')
      }
      const member = JSON.parse(localStorage.getItem("loginedMember"))
      alert(member)
      member.password = changedPassword
      alert(JSON.stringify(member))
      
      memberModify({member})
      .then(res => {
        console.log(`비밀번호 수정 완료 : ${res.data.result} `)
        localStorage.setItem("loginedMember", JSON.stringify(member))
        history.push('/member-list')
        
      })
      .catch(err => {
        console.log(`비밀번호 수정 실패 : ${err} `)
  
      })
    }

    return (<>
    <div className="modify"></div>
    <form method="PUT" onSubmit={handleSubmit} >
            
                <h2 style={{"text-align":"center"}}>비밀번호 수정</h2>
        <div className="container">
          <label labelFor="psw"><b>변경할 비밀번호</b></label>
          <input type="password" placeholder="Enter Password" onChange={e => {setChangedPassword(e.target.value)}} name="password" required/>
              
          <button type="submit">확 인</button>
         
        </div>

      </form>

       
      </>)
}

export default MemberModifyForm