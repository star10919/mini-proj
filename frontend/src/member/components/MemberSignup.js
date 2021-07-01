import React,{useState} from 'react'
import '../styles/Signup.css'
import { Button } from '@material-ui/core';
import { source } from 'axe-core';
import { memberLogin, memberRegister, memberSignup } from 'api';
import { useHistory } from 'react-router'
const SignUp = () => {
  const history = useHistory()
  const [userInfo, setUserInfo] = useState({
    username: '',
    password: '',
    name: '',
    email: ''
  })

  const {username, password, name, email} = `userInfo`

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo,
      [name]: value
    })
  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송 클릭: ${JSON.stringify({...userInfo})}`)
    memberRegister({...userInfo})
    .then(res => {  //성공했을 때, 프로미스 사용
      alert(`회원가입 완료 : ${res.data.result} `)
      // history.push('login')
    })
    .catch(err => { //실패했을 때, 프로미스 사용
      alert(`회원가입 실패 : ${err} `)
    })
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }


    return (<>
    <div className="Signup">
    <form onSubmit={handleSubmit} method="get" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>Sign Up</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>

        <label for="username"><b>User ID</b></label>
        <input type="text" placeholder="Enter ID" onChange={handleChange} name="username" value={username} />

        <label for="password"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" onChange={handleChange} name="password"  value={password}/>

        <label for="name"><b>Name</b></label>
        <input type="text" placeholder="Enter Your Name" onChange={handleChange} name="name"  value={name}/>

        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" onChange={handleChange} name="email"  value={email}/>

        <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

        <div class="clearfix">
          <button type="submit" className="signupbtn">Sign Up</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
        
      </div>
    </div>
  </form>
</div>
</>)
}

export default SignUp