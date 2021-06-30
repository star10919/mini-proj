import React,{useState} from 'react'
import './PostWrite.css'
import { postWrite } from 'api'
import { Button } from '@material-ui/core';
import { source } from 'axe-core';
import { useHistory } from 'react-router'

const PostWrite = () => {
  const [userPost, setUserPost] = useState({
    title: '',
    content: ''
  })

  const {title, content} = `userPost`

  const handleChange = e => { //event 3대장
    const { name:name, value:value } = e.target
    setUserPost({
      ...userPost,
      [name]: value
    })
  }

  const handleSubmit = e => { //event 3대장
    e.preventDefault()     //반드시 해야함
    alert(`전송 클릭: ${JSON.stringify({...userPost})}`)
    postWrite({...userPost})
    .then(res => {
      alert(`게시글 등록 : ${res.data.result}`)
    })
    .catch(err => {
      alert(`게시글 등록 실패: ${err} `)
    })
  }

  const handleClick = e => {  //event 3대장
    e.preventDefault()    //반드시 해야함
    alert('취소 클릭')
  }


    return (<>
    <div className="PostWrite">
    <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>게시글 쓰기</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>

        <label for="title"><b>title</b></label>
        <input type="text" placeholder="Enter title" onChange={handleChange} name="title" value={title} />

        <label for="content"><b>content</b></label>
        <input type="text" placeholder="Enter content" onChange={handleChange} name="content"  value={content}/>

        <p>By creating an account you agree to our <a href="#" style={{color:"dodgerblue"}}>Terms & Privacy</a>.</p>

        <div class="clearfix">
          <button type="submit" className="submitbtn">submit</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
        
      </div>
    </div>
  </form>
</div>
</>)
}

export default PostWrite