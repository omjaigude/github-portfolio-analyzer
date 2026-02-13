async function analyze(){

const username=document.getElementById("username").value

const res=await fetch(`http://127.0.0.1:8000/analyze/${username}`)
const data=await res.json()

document.getElementById("result").classList.remove("hidden")

document.getElementById("name").innerText=data.user
document.getElementById("stats").innerText=`Followers: ${data.followers} | Repos: ${data.repos}`

document.getElementById("score").innerText=`Score: ${data.analysis.score}`
document.getElementById("grade").innerText=` (${data.analysis.grade})`

let ul=document.getElementById("report")
ul.innerHTML=""
for(const key in data.analysis.report){
let li=document.createElement("li")
li.innerText=key+" : "+data.analysis.report[key]
ul.appendChild(li)
}

let review=data.review
document.getElementById("review").innerHTML=`
<b>Strengths:</b><br>${review.strengths.join("<br>")}<br><br>
<b>Weaknesses:</b><br>${review.weaknesses.join("<br>")}<br><br>
<b>Advice:</b><br>${review.advice.join("<br>")}<br><br>
<b>Final Decision:</b> ${review.decision}
`
}
