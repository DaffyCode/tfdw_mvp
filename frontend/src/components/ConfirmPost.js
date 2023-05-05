import { Col, Container, Row } from 'react-bootstrap';
import {  useLocation, useNavigate } from 'react-router-dom';

const ConfirmPost = () => {

  const navigate = useNavigate();
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const commentText = searchParams.get('comment');
  const category = searchParams.get('category');
  const size = searchParams.get('size');
  const color = searchParams.get('color');
  const amount = searchParams.get('amount');
  const commentText2 = searchParams.get('comment2');
  const category2 = searchParams.get('category2');
  const size2 = searchParams.get('size2');
  const color2 = searchParams.get('color2');
  const amount2 = searchParams.get('amount2');


  const handleGoBack = () => {
    navigate('/setpost');
  };
  return (
    <Container>
    <div className='dashboard'>
        <div className="text-center">
            <Row>
                <Col sm={2} >
                    <button className='home-image'></button></Col>
                <Col sm={8}>
                    <h4>Spendenplatform</h4></Col>
                <Col sm={2} >
                    <button className='konto-image'></button></Col>
            </Row>
        </div>
        <div className='donation-articles'>
              <div id='post-width'>
            
             <Row> {category || size || color || amount && amount !== "0" || commentText ? (   <>
   
                 <h6>Spendendetails</h6>
               
                <Col>
                <select className='filters'>
                <option value='' disabled selected>{category}</option>
                    <option value="jersey_kit">Trikot Set</option>
                    <option value="jersey_top">Trikot Oberteil</option>
                    <option value="tracksuit_top">Trainingsanzug Oberteil</option>
                    <option value="shoes">Schuhe (Paar)</option>
                    <option value="football_sock">Stutzen</option>
                    <option value="bib">Leibchen</option>
                    <option value="gloves">Handschuhe (Paar)</option>
                </select></Col>
                <Col><select className='filters'>
                <option value='' disabled selected>{size}</option>
                    <option value="adult">Adult</option>
                    <option value="children">Kids</option>
                </select> </Col>
                <Col><select className='filters'>
                <option value='' disabled selected>{color}</option>
                    <option value="red">Rot</option>
                    <option value="yellow">Gelb</option>
                    <option value="green">Grün</option>
                    <option value="blue">Blau</option>
                    <option value="white">Weiß</option>
                    <option value="orange">Orange</option>
                </select></Col>
                <Col><select className='filters'>
                <option value='' disabled selected>{amount}</option>

                </select></Col>
          
              
                <Col>
           <div className='text-areas'>
           <textarea type='text' className='commentbox' 
              value={commentText}>{commentText}</textarea></div>   
              </Col>  </>
               ) : null}
           </Row>

          
<Row>

  {category2 || size2 || color2 || amount2 && amount2 !== "0" || commentText2 ? (
   
    <> <div className='straight-line'></div>
    <h6>Spendendetails</h6>
      <Col>
        <select className="filters">
          <option value="" disabled selected>
            {category2}
          </option>
                    
                    <option value="jersey_kit">Trikot Set</option>
                   <option value="jersey_top">Trikot Oberteil</option>
                   <option value="tracksuit_top">Trainingsanzug Oberteil</option>
                   <option value="shoes">Schuhe (Paar)</option>
                   <option value="football_sock">Stutzen</option>
                   <option value="bib">Leibchen</option>
                   <option value="gloves">Handschuhe (Paar)</option>
        </select>
      </Col>
      <Col>
        <select className="filters">
          <option value="" disabled selected>
            {size2}
          </option>
          <option value="adult">Adult</option>
                <option value="children">Kids</option>
        </select>{" "}
      </Col>
      <Col>
        <select className="filters">
          <option value="" disabled selected>
            {color2}
          </option>
          <option value="red">Rot</option>
               <option value="yellow">Gelb</option>
               <option value="green">Grün</option>
               <option value="blue">Blau</option>
               <option value="white">Weiß</option>
               <option value="orange">Orange</option>
        </select>
      </Col>
      <Col>
        <select className="filters">
          <option value="" disabled selected>
            {amount2}
          </option>
        </select>
      </Col>
      <Col>
        <div className="text-areas">
        <textarea type='text' className='commentbox' 
              value={commentText}>{commentText}</textarea>
        </div>
      </Col>
    </>
  ) : null}
</Row>

     <div className='setpost-buttons'>
            <button className='button-pink' >Bestätigen</button>
            <button className='button-pink' onClick={handleGoBack}>Züruck</button>
           
            {/* the fields can be edited without needing this button
            <button className='button-pink' >Bearbeiten</button>   */}
    </div>
    </div>     
    </div>
        </div>
     
</Container>
    
  );
};
export default ConfirmPost