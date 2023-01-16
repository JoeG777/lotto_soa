# lotto_soa

### Anforderungen
[Aufgabenstellung](https://moodle.thi.de/course/view.php?id=7642&section=1)

1. Zwei Dienste mit Datenerfassung
Das vorliegende Beispiel realisiert zwei Service:
    - [drawing_service](./drawing_service/)
    - [customer_service](./customer_service/)

    Dabei persistiert der _customer_service_ einige der Daten in einer [NoSQL MongoDB-Datenbank](https://www.mongodb.com/) über einen entsprechenden [Adapter](./customer_service/src/customer/application/db_client.py)

2. Einer der Dienste ist durch einen modernen Architekturansatz realisiert
    - _TBD_

3. Dokumentation der Installation des Services auf einer VM

    [Anleitung](#installation-der-anwendung-auf-einer-vm) zur Installation und Ausführung des Systems in einer VM

4. Dockerfiles inklusive Dokumentation der Auführung dieser mit bestehenden Daten
    - _TBD_

5. Docker Compose der Services, Dokumentation der Ausführung, NGNIX als Load Balancer
    [Dokumentation der Ausführung](./infrastructure/README.md)

6. Kubernetes Manifeste
    - _TBD_

7. Automatisierung des Bauprozesses
    - _TBD_
    
8. Skizze der Service-Architektur
    - _TBD_

---

### Installation der Anwendung auf einer VM
Annahme an Vorbedingunge: 
 - stabile Linux-Version
 - VM aktualisiert und upgegraded

1. Installation Python
2. Installation MongoDB
3. Installation RabbitMQ
4. Verschieben des Source-Codes in den Speicher der VM
5. Konfiguration entsprechend der Dokumentation (Referenz auf einzelen READMEs)
6. Starten der Services