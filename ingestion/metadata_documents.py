documents = [
    {
        "id": "shipment_tracking_table",
        "type": "table",
        "text": {
            "table": "shipment_tracking",
            "description": "Contains the latest tracking information for shipments including location, ETA, status, carrier and rerouting information.",
            "columns": [
                "shipment_id",
                "location",
                "eta",
                "status",
                "carrier",
                "reroute_mode_if_any_disruption"
            ]
        }
    },
    {
        "id": "shipment_tracking_location",
        "type": "column",
        "text": {
            "table": "shipment_tracking",
            "column": "location",
            "description": "Current known shipment location.",
            "aliases": [
                "current location",
                "where is shipment",
                "shipment location",
                "current warehouse",
                "current city"
            ]
        }
    },
    {
        "id": "shipment_tracking_status",
        "type": "column",
        "text": {
            "table": "shipment_tracking",
            "column": "reroute_mode_if_any_disruption",
            "description": "Rerouting the shipments if any potential disruptions.",
            "aliases": [
                "re-routing mode",
                "disrupted or distorted shipment preferred mode for rerouting"
            ]
        }
    },
    {
        "id": "shipment_tracking_status",
        "type": "column",
        "text": {
            "table": "shipment_tracking",
            "column": "status",
            "description": "Current shipment status.",
            "aliases": [
                "tracking status",
                "delivery status",
                "shipment progress"
            ]
        }
    },
    {
        "id": "shipment_tracking_sql_example_1",
        "type": "sql_example",
        "text": {
            "question": "Where is shipment SHP1001?",
            "sql": "SELECT location,status FROM shipment_tracking WHERE shipment_id='SHP1001';"
        }
    }
]