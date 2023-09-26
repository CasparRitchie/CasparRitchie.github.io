import axios from 'axios';
import React, { useState, useEffect } from 'react';

function AuditConstatPage() {
    const [audits, setAudits] = useState([]);
    const [selectedAudit, setSelectedAudit] = useState(null);
    const [constats, setConstats] = useState([]);

    useEffect(() => {
        // Fetch audits when the component mounts
        fetchAudits();
    }, []);

    const fetchAudits = async () => {
        try {
            const response = await axios.get('/audits/');
            setAudits(response.data);
        } catch (error) {
            console.error("Error fetching audits:", error);
        }
    };

    const handleCreateAudit = async () => {
        // Logic to create a new audit
        // For demonstration purposes, let's assume we send an object with some data
        const newAuditData = {
            // dummy data for demonstration
            title: "New Audit",
            // ... any other data you need for the audit
        };

        try {
            await axios.post('/audits/', newAuditData);
            fetchAudits(); // Refresh audits after creating a new one
        } catch (error) {
            console.error("Error creating new audit:", error);
        }
    };

    const handleSelectAudit = async (auditId) => {
        setSelectedAudit(audits.find(a => a.id === auditId));
        fetchConstats(auditId);
    };

    const fetchConstats = async (auditId) => {
        try {
            const response = await axios.get('/constats/audit/${auditId}/');
            setConstats(response.data);
        } catch (error) {
            console.error("Error fetching constats for audit:", error);
        }
    };

    const handleCreateConstat = async () => {
        // Logic to create a new constat for the selected audit
        // For demonstration purposes, let's assume we send an object with some data
        const newConstatData = {
            description: "New Constat",
            auditId: selectedAudit.id,
            // ... any other data you need for the constat
        };

        try {
            await axios.post('/constats/', newConstatData);
            if (selectedAudit) {
                fetchConstats(selectedAudit.id); // Refresh constats after creating a new one
            }
        } catch (error) {
            console.error("Error creating new constat:", error);
        }
    };

    return (
        <div>
            <h2>Gestion Audits et Constats</h2>

            <section>
                <h3>Créer un Audit</h3>
                <button onClick={handleCreateAudit}>Nouvel Audit</button>
            </section>

            <section>
                <h3>Les Audits</h3>
                <ul>
                    {audits.map(audit => (
                        <li key={audit.id} onClick={() => handleSelectAudit(audit.id)}>
                            {audit.title}  {/* Assuming each audit has a title */}
                            {/* You can add more details or styles to show which audit is currently selected */}
                        </li>
                    ))}
                </ul>
            </section>

            {selectedAudit && (
                <section>
                    <h3>Constats pour l'Audit {selectedAudit.title}</h3>
                    <button onClick={handleCreateConstat}>Ajouter Constat</button>
                    <ul>
                        {constats.map(constat => (
                            <li key={constat.id}>
                                {constat.description}  {/* Assuming each constat has a description */}
                                {/* Add more details or operations for each constat */}
                            </li>
                        ))}
                    </ul>
                </section>
            )}
        </div>
    );
}

export default AuditConstatPage;
