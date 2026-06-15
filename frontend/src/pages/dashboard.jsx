import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        api.get("/alerts")
            .then((response) => {
                setAlerts(response.data);
            })
            .catch((error) => {
                console.error("Failed to fetch alerts:", error);
            });
    }, []);

    return (
        <div style={{ padding: "20px" }}>
            <h1>Advanced SIEM Dashboard</h1>

            <h2>Alerts</h2>

            <table border="1" cellPadding="10">
                <thead>
                    <tr>
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
    );
}

export default Dashboard;