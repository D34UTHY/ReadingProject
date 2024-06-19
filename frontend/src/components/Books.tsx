import React, { useState, useEffect } from 'react';
import api from '../api';

interface Livro {
    id: number;
    titulo: string;
    descricao: string;
    autor: string;
    categoria: string;
    dataPublicacao: string;
}

const Livros: React.FC = () => {
    const [livros, setLivros] = useState<Livro[]>([]);

    useEffect(() => {
        api.get('/livros').then(response => {
            setLivros(response.data);
        });
    },  []);

    return (
        <div>
            <h1>Livros</h1>
            <ul>
                {livros.map(livro => (
                    <li key={livro.id}>{livro.titulo}</li>
                ))}
            </ul>
        </div>
    );
};

export default Livros;