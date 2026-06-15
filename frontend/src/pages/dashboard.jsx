import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
    const [alerts, setAlerts] = useState([]);
    const [selectedAlert, setSelectedAlert] = useState(null);

    useEffect(() => {
        api.get("/alerts")
            .then((response) => {
                setAlerts(response.data);
            })
            .catch((error) => {
                console.error("Failed to fetch alerts:", error);
            });
    }, []);

    const openAlertDetails = (alertId) => {
        api.get(`/alerts/${alertId}`)
            .then((response) => {
                setSelectedAlert(response.data);
            })
            .catch((error) => {
                console.error("Failed to fetch alert details:", error);
            });
    };

    return (
        <div style={{ padding: "20px" }}>
            <h1>Advanced SIEM Dashboard</h1>
<h3>VERSION 8.3 TEST</h3>
            <h2>Alerts</h2>
            <p >Total alerts: {alerts.length}</p>
            <div style={{ overflowX: "auto", maxWidth: "100%" }}>
            <table border="1" cellPadding="10" style={{ minWidth: "900px" }}>
                <thead>
                    <tr>
                        <th>Action</th>
                        <th>Attack Type</th>
                        <th>Severity</th>
                        <th>Status</th>
                        <th>Username</th>
                        <th>Source IP</th>
                    </tr>
                </thead>

                <tbody>
                    {alerts.map((alert) => (
                        <tr key={alert.alert_id}>
                            <td>
                                <button
                                    onClick={() => openAlertDetails(alert.alert_id)}
                                >
                                    Investigate
                                </button>
                            </td>

                            <td>{alert.attack_type}</td>
                            <td>{alert.severity}</td>
                            <td>{alert.status}</td>
                            <td>{alert.username}</td>
                            <td>{alert.source_ip}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            </div>

            {selectedAlert && (
                <div style={{
                    marginTop: "30px",
                    padding: "20px",
                    border: "1px solid #333"
                }}>
                    <h2>Alert Investigation</h2>

                    <p><strong>Alert ID:</strong> {selectedAlert.alert_id}</p>
                    <p><strong>Attack Type:</strong> {selectedAlert.attack_type}</p>
                    <p><strong>Severity:</strong> {selectedAlert.severity}</p>
                    <p><strong>Confidence:</strong> {selectedAlert.confidence}</p>
                    <p><strong>Status:</strong> {selectedAlert.status}</p>
                    <p><strong>Username:</strong> {selectedAlert.username}</p>
                    <p><strong>Source IP:</strong> {selectedAlert.source_ip}</p>
                    <p><strong>Hostname:</strong> {selectedAlert.hostname}</p>
                    <p><strong>Failed Attempts:</strong> {selectedAlert.failed_attempts}</p>
                    <p><strong>Message:</strong> {selectedAlert.message}</p>

                    <h3>Evidence Event IDs</h3>
                    <ul>
                        {selectedAlert.evidence_event_ids.map((id) => (
                            <li key={id}>{id}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default Dashboard;