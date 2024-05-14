import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Form() {
    const [campos, setCampos] = useState({
        txtNome: ''
    });

    const [ret, setRet] = useState('');

    function handleInputChange(event) {
        if (event === undefined) {
            console.log('Evento indefinido');
        } else {
            campos[event.target.name] = event.target.value;
            console.log(event.target.name)
            setCampos(campos);
        }
    }

    function handleFormSubmit(event) {
        event.preventDefault();
        console.log(campos);
        axios.post('http://localhost:5000/api/formulario', campos).then(response => {
           setRet(response.data); 
        })
    }

    return (
        <div>
            <form onSubmit={handleFormSubmit}>
                <fieldset>
                    <legend>
                        <h2>Formulário de cadastro</h2>
                    </legend>
                    <div>
                        <label>Nome:</label>
                        <input type='text' name='txtNome' id='txtNome' onChange={handleInputChange}></input>
                    </div>
                    <input type='submit' value='Salvar'></input>
                    <div><p>Retornou: {ret}</p></div>
                </fieldset>
            </form>
        </div>
    )
}

export default Form;