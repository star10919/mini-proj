import React, {useState} from 'react'
import { Button } from '@material-ui/core';
import { memberLogin, userLogin } from 'api'
import '../styles/MemberLogin.css'

const MemberLogin = () => {
  const [loginInfo, setLoginInfo] = useState({
    username: '',
    password: ''
  })

  const { username, password } = `loginInfo`

  const handleChange = e => {
    const { name, value } = e.target
    setLoginInfo({
      ...loginInfo,
      [name]: value
    })
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송 클릭: ${JSON.stringify({...loginInfo})}`)
    memberLogin({...loginInfo})
    .then(res => {
      alert(`로그인 성공 : ${res.data.result} `)
    })
    .catch(err => {
      alert(`로그인 실패: ${err} ` )
    })
  }

return (<>
    <h2>Login Form</h2>
<div className="MemberLogin">
<form onSubmit={handleSubmit} method="GET">
  <div className="imgcontainer">
    <img src="https://www.w3schools.com/howto/img_avatar2.png" style={{width: "300px"}} alt="Avatar" className="avatar"/>
  </div>

  <div className="container">
    <label for="username"><b>Username</b></label>
    <input type="text" placeholder="Enter ID" onChange={handleChange} name="username" value={username} />

    <label for="password"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" onChange={handleChange} name="password"  value={password}/>
        
    <label>
      <input type="checkbox" checked="checked" name="remember"/> Remember me</label>
  </div>

  <div className="container" style={{backgroundColor: "#f1f1f1"}}>
    <Button type="submit" className="loginbtn">Login</Button>
    <Button type="button" className="cancelbtn">Cancel</Button>
    <span className="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
</div>

   
    </>)
}

export default MemberLogin