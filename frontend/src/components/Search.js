import React, { useState } from 'react';
import './Search.css';
import Pagination from '@mui/material/Pagination';
import Stack from '@mui/material/Stack';



import search_icon from "./icon.png"

const Search = (props) => {

    const [enteredSearch, setenteredSearch] = useState('');
    const [data, setData] = useState([]);
    const [relFeedback, setRelFeedback] = useState([])
    const [nonRelFeedback, setNonRelFeedback] = useState([])
    const [precisions, setPrecisions] = useState([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    const [totalRel, setTotalRel] = useState([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    const [rel_ids, setrel_ids] = useState([])
    const [nonrel_ids, setnonrel_ids] = useState([])
    const [currPage, setCurrPage] = useState(1);

    const SearchChangeHandler = (event) => {
        setenteredSearch(event.target.value);
    };

    const SearchHandler = async (event) => {
        event.preventDefault();

        setPrecisions([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        setTotalRel([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        fetch('http://127.0.0.1:8000/search/', {
            method: 'post',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                "entered_query": enteredSearch
            })
        }).then(res => res.json()).then(data =>{
            console.log(data.data)
            setData(data.data)
    });
    
        const SearchedData = {
            search: enteredSearch,
        };

        console.log(SearchedData);
    }

    // console.log(relFeedback)
    // console.log(nonRelFeedback)

    const addRel = async(id, index) => {
        // let temp = relFeedback
        // temp.push(id)
        // if(nonrel_ids.includes(id)){
        //     const indc = array.indexOf(5);
        //     if (indc > -1) { // only splice array when item is found
        //         array.splice(index, 1); // 2nd parameter means remove one item only
        //     }
        // }
        if(!rel_ids.includes(id))
            setrel_ids(rel_ids.concat(id))
        // await fetch('http://127.0.0.1:8000/feedback/', {
        //     method: 'post',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({
        //         "entered_query": enteredSearch,
        //         "rel_ids":rel_ids,
        //         "nonrel_ids":nonrel_ids,
        //         "choice":1
        //     })
        // }).then(res => res.json()).then(data =>{
        //     console.log(data.data)

        //     setData(data.data)}
        // );
        setRelFeedback([...relFeedback, id])
        // console.log(relFeedback);
        let rels = totalRel
        for (let i = index; i < 15; i++) {
            if (rels[i] >= i + 1) {
                rels[i] = i + 1
                break;
            }
            else rels[i] += 1
        }
        setTotalRel(rels)
        // console.log(rels);
        let temp = []
        for (let i = 0; i < 15; i++) {
            let prec = rels[i] / (i + 1)
            temp.push(prec);
        }

        // console.log(temp);

        setPrecisions(temp)
    }

    const addNonRel = (id, index) => {
        // let temp = nonRelFeedback
        // temp.push(id)
        // if(!nonrel_ids.includes(id))
        //     setnonrel_ids(nonrel_ids.concat(id))
        // fetch('http://127.0.0.1:8000/feedback/', {
        //     method: 'post',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({
        //         "entered_query": enteredSearch,
        //         "rel_ids":rel_ids,
        //         "nonrel_ids":nonrel_ids,
        //         "choice":1
        //     })
        // }).then(res => res.json()).then(data =>{
        //     console.log(data.data)
        //     setData(data.data)}
        // );
        let rels = totalRel
        for (let i = index; i < 15; i++) {
            if (rels[i] === 0) rels[i] = 0;
            else rels[i] -= 1
        }
        setTotalRel(rels)

        let temp = []
        for (let i = 0; i < 15; i++) {
            let prec = rels[i] / (i + 1)
            temp.push(prec);
        }
        setPrecisions(temp)
        setNonRelFeedback([...nonRelFeedback, id])
    }
    console.log(currPage)
    return (
        <div >
            <div className="container-heading "><h1 className='heading '>Search Blogs</h1></div>
            <div className='container'>

                <form onSubmit={SearchHandler} className='search-bar'>
                <input type="text" id="search" placeholder="Search for..." value={enteredSearch} onChange={SearchChangeHandler} required/>
                    <button type='submit' className = {"search_icon"}><img src={search_icon} /></button>
                    
                    {/* <label htmlFor="Search">Search Your Query Here</label><br />

                <input type="text" id="Search" name="Search" value={enteredSearch} onChange={SearchChangeHandler} />
                <br /> */}

                    {/* <div>
                    <button type='Search'>Search</button>
                </div> */}
                
            </form>
            </div>
            {/* {console.log(data.data)} */}
            {
                data.map((d,idx) => {
                    console.log(idx)
                    if (idx>=((currPage-1)*10) && idx<(currPage*10))
                    return (
                        <Card totalRel={totalRel} precisions={precisions} index={idx} key={d.id} d={d} addRel={addRel} addNonRel={addNonRel} />
                    )
                    // console.log(d);
                })
            }
            <Stack alignItems="center">
            <Pagination className='pagination' count={Math.ceil(data.length/10)} onChange={(e,p)=>setCurrPage(p)} showFirstButton showLastButton />
            </Stack>
        </div>
    );
};

function Card(props) {

    // const d = props.d

    const addRel = () => {
        props.addRel(props.d.id, props.index);
    };

    const addNonRel = () => {
        props.addNonRel(props.d.id, props.index);
    };
    console.log(props.d)
    return (
        <div>
            <div className='abc'>
                <hr />
                <h3>{props.d[0][4]}</h3>
                <h4>{props.d[0][5]}</h4>
                <h4>Precision : {props.precisions[props.index]}</h4>
                <h4>{props.d[0][6]}</h4>
                <button onClick={addRel} className='rel'>Relevance</button>
                <button onClick={addNonRel} className='Non-rel'>Non Relevance</button>

                <hr />
            </div>
        </div>
    )
}

export default Search;

