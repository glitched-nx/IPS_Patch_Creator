# Versionshinweise

## Sigpatches
**Erstellt am:** 2023-10-16T16:08:19Z

Überlagerbare Kerndateien des Atmosphère-Dreierpakets (fünfte Version von Atmosphère 1.8.0)

https://github.com/AK478BB/Sigpatches/releases

https://codeberg.org/ak478/AK-Atmosphere/releases

https://pan.baidu.com/s/1ZXq-AQhGAOtLOJIOZyKYRw?pwd=tpz6

Die überlagerbaren Kerndateien des Atmosphère-Dreierpakets können direkt auf Atmosphère 1.0.0 oder spätere Integrationspakete angewendet werden, ohne deine Atmosphère-Einstellungen zu ändern (wenn deine ursprünglichen Atmosphère-Einstellungsdateien fehlerhaft sind, bleiben sie auch nach dem Update fehlerhaft. Korrekte Einstellungsdateien findest du unter atmosphere/config_templates/). Es werden lediglich die Kerndateien von Atmosphère, Hekate und Sigpatch aktualisiert. Das einzige, worauf du achten musst, ist die Benennung der Startdatei bootloader/payloads/fusee.bin in der Hekate_ipl.ini-Einstellungsdatei. Einige Integrationspakete benennen fusee.bin in atmosphere.bin um. Da der Autor von Atmosphère ab Version 1.7.0 die KIP-Funktion entfernt hat, was das Laden von FS- und Loader-Patches beeinflusst, wird empfohlen, künftig den FSS0-Start von Atmosphère+Hekate zu verwenden oder das sys-patch-Plugin als Ersatz für die aktuelle Sigpatch-Funktion zu nutzen.

Am 2024.10.21 wurde die fünfte Version des Atmosphère 1.8.0 Dreierpakets veröffentlicht. Sigpatch hat auf der Grundlage von ES, FS, Loader und NFIM einen neuen Nim-Patch hinzugefügt. Dieser Nim-Patch eignet sich für die Verwendung eines Proxy-Servers im virtuellen System, um versteckte Seriennummern zu verwenden und den Zugang zu inoffiziellen Shops, YouTube und anderen Diensten zu ermöglichen, ohne gebannt zu werden. 【AK杂谈】führt dich Schritt für Schritt in die Atmosphère Sigpatch Signatur-Patches ein.

【Einführung in das Atmosphère-Dreierpaket】

Unterstützt maximal das Switch 19.0.0-System

(1) Atmosphère-1.8.0-preprerelease-c6014b533+hbl-2.4.4+hbmenu-3.6.0

https://github.com/Atmosphere-NX/Atmosphere/releases

https://www.tekqart.com/thread-382514-1-1.html

(2) Hekate_ctcaer_6.2.2_Nyx_1.6.4

https://github.com/CTCaer/hekate/releases

"Bootloader/sys/nyx.bin Backup" ist die englische Originaldatei, die das englische Original von Hekate6.2.2 wiederherstellen kann.

Die folgenden beiden Entwickler haben jeweils eine chinesische nyx.bin-Datei geteilt. Wähle eine nyx.bin-Datei aus und ersetze sie im bootloader/sys/-Verzeichnis.

https://github.com/easyworld/hekate/releases

https://www.tekqart.com/thread-222735-1-1.html

(3) Sigpatches für Atmosphère 1.8.0 (unterstützt maximal das SW19.0.0-System)

Es gibt mehrere Quellen, um die Signatur-Patches Sigpatch herunterzuladen.

https://gbatemp.net/threads/sigpatches-for-atmosphere-hekate-fss0-fusee-package3.571543/

https://hackintendo.com/download/sigpatches/

https://github.com/fraxalotl/SwitchScript

Adresse des neuen Nim-Patch-Patches

https://github.com/fruityloops1/nim-prodinfo-blank-fix/releases

Signatur-Patch-Erstellungstool IPS_Patch_Creator

https://github.com/mrdude2478/IPS_Patch_Creator/releases

https://disk.yandex.com/d/LEKGKbfDw-_pjA

Das sys-patch-Plugin, das in atmosphere/contents gestartet wird, kann auch die oben genannten IPS-Format-Signatur-Patches ersetzen.

https://github.com/ITotalJustice/sys-patch/releases

【Zwei, Payload-Plugins】

(1) CommonProblemResolver--v0.3.5

Unter Hekate können Themen gelöscht und das automatische Starten von Plugins deaktiviert werden, OLED-kompatibel.

Option 1 deaktiviert das automatische Starten von Plugins, Option 2 löscht installierte Themen und löst effektiv das Problem, dass das HOS-System nicht gestartet werden kann.

https://github.com/zdm65477730/CommonProblemResolver/releases

(2) Lockpick_RCM--v1.9.13

Ein Tool zur Extraktion von Konsolensystemschlüsseln, OLED-kompatibel.

Die extrahierten prod.keys befinden sich auf der SD-Karte im Switch/-Verzeichnis.

https://github.com/Decscots/Lockpick_RCM/releases

(3) TegraExplorer--v4.2.0

Ein Dateiverwaltungstool unter Hekate, OLED-kompatibel.

https://github.com/suchmememanyskill/TegraExplorer/releases

Nützliche Tegraexplorer-Programmskripte

https://github.com/suchmememanyskill/TegraScript

https://github.com/JeffVi/Prodinfo-Restore-TegraScript

(4) hwfly_toolbox--v1.1.1

Ein Toolset für hwfly-Chips, speziell für hwfly-Chip-Hardbreaks, das ein Firmware-Update des hwfly-Chips ohne Demontage ermöglicht.

Notwendig für das Spielen von Lakka, Ubuntu und Android.

Nach dem Upgrade des Originalsystems muss der sdloader.enc erneut geflasht werden, das Upgrade des virtuellen Systems hat keinen Einfluss.

https://github.com/hwfly-nx/hwfly-toolbox/releases

Nach dem Flashen von sdloader.enc kann das System ohne eingelegte SD-Karte gestartet werden, indem nach dem Einschalten die Lautstärketasten + und - gedrückt werden, um das Originalsystem zu starten.

Entpacke und kopiere sdloader.enc in das Stammverzeichnis der SD-Karte.

https://github.com/hwfly-nx/firmware/releases

(5) picofly_toolbox--v0.2

Ein Toolset für Raspberry Pi-Chips, speziell für rp2040-Chip-Hardbreaks, das ein Firmware-Update des sdloader und der Raspberry Pi-Firmware ohne Demontage ermöglicht.

Das Upgrade der Raspberry Pi-Firmware erfolgt über die Datei update.bin im Stammverzeichnis. Wenn das System normal startet, ist kein Upgrade der Raspberry Pi-Firmware erforderlich.

https://github.com/rehius/usk/releases

https://github.com/Ansem-SoD/Picofly/tree/main/Firmwares

【Drei, Methode zur Aktualisierung des AK Atmosphère-Kernpakets mit dem überlagerbaren Dreierpaket】

atmosphere/config_templates/ enthält alle Einstellungsdateivorlagen, die in diesem Verzeichnis nicht wirksam werden.

1. Kopiere system_settings.ini, override_config.ini, stratosphere.ini nach atmosphere/config/

2. Kopiere exosphere.ini in das Stammverzeichnis

3. Kopiere den Ordner hosts nach atmosphere/

4. Kopiere den Ordner bootloader in das Stammverzeichnis

Das AK Atmosphère-Kernpaket ist das minimal funktionsfähige Atmosphère-Integrationspaket, das alle installierten Spiele spielen kann und das stabilste Atmosphère-Integrationspaket ist.

Wenn neue Spiele oder andere Funktionen installiert werden müssen, können Plugins wie dbi.nro, Tesla usw. hinzugefügt werden.

【Vier, Aktualisierung und Startkonfiguration des AK Atmosphère-Kernpakets】

(1) Wenn du derzeit das AK Original Atmosphère 1.3.0 oder spätere persönliche Integrationspakete verwendest und keine anderen Plugins hinzugefügt hast, kannst du das neue AK Atmosphère-Integrationspaket direkt überlagern.

Wenn Plugins hinzugefügt wurden, kannst du die alten Verzeichnisse atmosphere/contents, config und switch/.overlays auf der Speicherkarte löschen und dann das neue AK Atmosphère-Integrationspaket überlagern.

Wenn beim Überlagern auf ein anderes Integrationspaket Probleme auftreten, ist es am sichersten, die Verzeichnisse nintendo und emummc beizubehalten und den Rest zu löschen, bevor das komprimierte Paket überlagert wird.

(2) Unabhängig davon, ob es sich um eine Softmod- oder Hardmod-Konsole handelt, erfolgt der Softmod durch Kurzschließen + Injektion beim Starten, der TX-Injektor wird direkt verwendet, der Atmosphère-Injektor ersetzt die integrierte Payload.bin. Wenn Hekate 4.2 oder höher integriert ist, ist kein Ersatz erforderlich. Der Hardmod erfolgt durch einfaches Drücken der Einschalttaste, danach gibt es keinen Unterschied zum Softmod.

Klicke auf Launch und wähle die gewünschte Option:

cfw(sysnand): Gehackter Zustand des realen Systems, FSS0-Start von Hekate, ermöglicht Originalmodifikationen.

cfw(emunand): Gehackter Zustand des virtuellen Systems, FSS0-Start von Hekate, ermöglicht gehackte Spiele.

ofw(sysnand): Nicht gehackter Zustand des realen Systems, FSS0-Start von Hekate, ermöglicht Original-Online-Spiele.

cfw(auto): Originaler Fusee-Start von Atmosphère, erkennt automatisch das reale und virtuelle System basierend auf emummc.ini.

Klicke auf More Configs und wähle die gewünschte Option:

Lakka-Erista: Der alte Lakka-Emulator, der ursprünglich von AK Atmosphère eingestellt wurde. Er unterstützt nur Softmod- oder gepatchte Konsolen, ist aber mit exFAT-SD-Karten kompatibel.

Lakka-l4t: Der neue Lakka-Emulator, kompatibel mit Mariko/OLED, unterstützt derzeit nur FAT32-SD-Karten.

ubuntu-l4t: Das neue Ubuntu-System, kompatibel mit Mariko/OLED, unterstützt derzeit nur FAT32-SD-Karten.

lockpick_rcm: Software zur Extraktion von Konsolenschlüsseln.

CommonProblemResolver: Software zur Behebung von Startproblemen der Konsole.

TegraExplorer: Software zur Dateiverwaltung der Konsole.
