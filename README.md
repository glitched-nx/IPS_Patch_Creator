【AK杂谈】Drei Lösungen für Sigpatch-Signatur-Patches nach Atmosphère 1.7.0

Ab Atmosphère 1.7.0 hat der Entwickler SciresM die KIP-Ladefunktion entfernt, die ursprünglich zum Schutz des Kartenschachts ohne GC gedacht war. Diese Funktion ist jedoch bereits im stratosphere.romfs-Kernel integriert und kann über stratosphere.ini eingestellt werden, sodass keine zusätzlichen Patches erforderlich sind. Das Entfernen der KIP-Funktion beeinflusst das Laden von FS-Patches und führt zu Problemen mit extremen Übertaktungen des loader.kip und anderen.

Derzeit gibt es drei Lösungen für dieses Problem:

(1) Da das Atmosphère-Dreierpaket aus Atmosphère, Hekate und Sigpatch besteht, gibt es vier Startmethoden. Der Fusee-Start von Atmosphère kann keine KIP-Patches mehr laden, aber durch den FSS0-Start von Hekate im realen (gehackten) System und im virtuellen (gehackten) System wird das KIP über bootloader/patch.ini implementiert, sodass es nicht von der Atmosphère 1.7.0-Aktualisierung betroffen ist, die das Spielen von gehackten Spielen verhindert.

https://www.tekqart.com/thread-289271-1-1.html

Von links nach rechts sind die ersten drei FSS0-Starts, der vierte ist der Fusee-Start.

(2) Sigpatch kann als IPS geladen werden oder durch das Plugin-Signatur-Patch-Verfahren von sys-patch, was bedeutet, dass keine Sigpatch-Komponenten erforderlich sind. Im gehackten System wird das sysmodule gestartet, und über Tesla kann ausgewählt werden, ob Sigpatch aktiviert werden soll, sodass gehackte Spiele gespielt werden können. Das sys-patch-Plugin unterstützt sowohl den Fusee- als auch den FSS0-Start, sodass im hekate_ipl.ini für den FSS0-Start kein kip1patch=nosigchk und kein patches.ini erforderlich sind.

Dieses Dreierpaket (oder man könnte sagen Viererpaket) besteht aus Atmosphère, Hekate, sys-patch und Tesla. Tesla wird verwendet, um das Menü von sys-patch aufzurufen.

Der Entwickler Lailei hat ein Atmosphère-Integrationspaket mit integriertem sys-patch-Plugin veröffentlicht.

https://www.tekqart.com/thread-391203-1-1.html

(3) Der Entwickler LSP hat die Kerndateien von Atmosphère 1.7.0 kompiliert, einschließlich atmosphere/package3, atmosphere/stratosphere.romfs und fusee.bin. Damit können die Einschränkungen des Loader-Patches entfernt und die FS-Patches von Sigpatch integriert werden.

https://www.tekqart.com/thread-382514-1-1.html

Alle drei Methoden sind gleichwertig, und es spielt keine Rolle, welche verwendet wird, da das Ergebnis dasselbe ist. Die erste Methode ist jedoch als Fortsetzung der bisherigen Praxis relativ einfach zu verwenden. Dies entspricht den von AK veröffentlichten Atmosphère-Dreierpaket-Dateien, die überlagert werden können.

https://www.tekqart.com/thread-321617-1-1.html

Es kann überlagert werden, solange im Hekate_ipl.ini der Fusee-Start (cfw auto) nicht ausgewählt wird, was als Lösung für das Spielen von gehackten Spielen nach Atmosphère 1.7.0 dient.

Sigpatch, auch bekannt als Atmosphère-Signatur-Patch, ermöglicht es dem Atmosphère-System, gehackte Spiele und Frontend-Software auszuführen.

ES-Patch, FS-Patch und Loader-Patch sind Signatur-Patches, während nfim ctest die Überprüfung durch Nintendo-Server umgeht.

(1) Der ES-Patch befindet sich auf der SD-Karte unter atmosphere/exefs_patches/es_patches und entspricht dem SW-System. Bei jedem großen SW-System-Upgrade wird ein neues IPS benötigt.

Es wird empfohlen, alte ES-Patches beizubehalten, da sie benötigt werden, wenn das System heruntergestuft wird, um gehackte Spiele zu spielen. Der ES-Patch ermöglicht die Installation und den normalen Betrieb von Original-NSP-Spieldateien (einschließlich des komprimierten Formats NSZ), die aus dem Eshop-Shop gedumpt wurden.

(2) Der FS-Patch befindet sich auf der SD-Karte unter atmosphere/kip_patches/fs_patches und entspricht dem SW-System. Bei jedem großen SW-System-Upgrade werden zwei neue IPS (exfat und fat32) benötigt.

Es wird empfohlen, alte FS-Patches beizubehalten, da sie benötigt werden, wenn das System heruntergestuft wird, um gehackte Spiele zu spielen. Der FS-Patch ermöglicht die Installation und den normalen Betrieb von nicht-originalen NSP-Dateien (NSP, NSZ, XCI, XCZ), einschließlich NRO-Plugins, die in das NSP-Format konvertiert wurden, sowie integrierte XCI- und NSP-Formate.

(3) Der Loader-Patch befindet sich auf der SD-Karte unter atmosphere/kip_patches/loader_patches und entspricht dem Atmosphère-Package3. Bei jedem Atmosphère-Upgrade wird ein neues IPS benötigt.

Alte Loader-Patches sind nutzlos und können gelöscht werden, da Atmosphère abwärtskompatibel ist und beim Herunterstufen des Systems keine Atmosphère-Dateien ersetzt werden müssen.

(4) Der nfim ctest befindet sich auf der SD-Karte unter atmosphere/exefs_patches/nfim_ctest und ist mit dem SW-System verbunden. Es wird empfohlen, alte nfim ctest beizubehalten.

(5) Das Atmosphère-System unterscheidet zwischen FSS0-Start (real, virtuell, Originalsystem) und Fusee-Start (automatische Erkennung).

Die FS- und Loader-Patches für den FSS0-Start befinden sich auf der SD-Karte unter bootloader/patches.ini und unterscheiden sich vom Fusee-Start.

Die ES-Patches und nfim ctest für den FSS0-Start sind identisch mit denen für den Fusee-Start und unterscheiden sich nicht.
