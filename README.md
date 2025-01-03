Cursor Trial Reset Tool
This tool is designed to reset identifiers (IDs) used by Cursor software and manage its configuration file. It offers a user-friendly experience with both automatic and manual methods, ensuring a seamless process with built-in safety measures, guidance, and rollback mechanisms.

Features:
Automatic Installation:
Automates the entire process with commands tailored to the user's operating system (Windows, macOS, Linux supported).

Manual Installation Guide:
Provides a detailed guide for manually editing the configuration file if the automatic method fails.

Safety Features:

Automatic configuration file backup.
Rollback mechanism for error recovery.
Comprehensive error handling during file operations.
Supported Systems:

Windows x64
macOS Intel & M Series
Linux x64 & ARM64
UUID Renewal:
Securely updates the following fields in the configuration file:

telemetry.machineId
telemetry.macMachineId
telemetry.devDeviceId
telemetry.sqmId
Usage Guide:
1. Automatic Installation:
Windows: Run PowerShell as an administrator and execute the following command:
powershell
Kodu kopyala
irm https://raw.githubusercontent.com/yuaotian/go-cursor-help/master/scripts/install.ps1 | iex
Linux/macOS:
Open a terminal and run the following command:
bash
Kodu kopyala
curl -fsSL https://raw.githubusercontent.com/yuaotian/go-cursor-help/master/scripts/install.sh | sudo bash
2. Manual Installation (If Automatic Fails):
Locate the Configuration File:
Windows: %APPDATA%\Cursor\User\globalStorage\storage.json
macOS: ~/Library/Application Support/Cursor/User/globalStorage/storage.json
Linux: ~/.config/Cursor/User/globalStorage/storage.json
Update UUID Fields:
Open the storage.json file in a text editor and replace the relevant fields with new UUIDs.
How It Works:
Step-by-Step Guidance:
The program provides explanations for each step during the process.

Fallback Options:
Offers manual solutions if the automatic process fails.

Developer-Friendly:
Open-source and highly customizable.

This tool is the perfect solution for resetting Cursor trial configurations.
For questions or contributions, feel free to reach out via this repository! 🌟

Türkçe Açıklama (README): Cursor Trial Reset Tool
Cursor Trial Reset Tool
Bu araç, Cursor yazılımında kullanılan kimlikleri (IDs) sıfırlamak ve yapılandırma dosyasını yönetmek için tasarlanmıştır. Kullanıcı dostu bir deneyim sunan araç, otomatik ve manuel yöntemlerle işlem yapma imkanı sağlar. Sorunsuz bir süreç sağlamak için güvenlik önlemleri, rehberlik ve geri dönüş mekanizmaları içerir.

Özellikler:
Otomatik Kurulum:
Kullanıcının işletim sistemine uygun bir komutla tüm süreci otomatik hale getirir (Windows, macOS, Linux desteklenir).

Manuel Kurulum Rehberi:
Otomatik kurulum başarısız olduğunda, yapılandırma dosyasını manuel olarak düzenlemek için detaylı bir rehber sunar.

Güvenlik Özellikleri:

Otomatik dosya yedekleme.
Hatalarda geri dönüş (rollback) mekanizması.
Dosya düzenleme işlemleri sırasında tam hata kontrolü.
Desteklenen Sistemler:

Windows x64
macOS Intel & M serisi
Linux x64 & ARM64
UUID Yenileme:
Yapılandırma dosyasındaki aşağıdaki alanları güvenli bir şekilde yeniler:

telemetry.machineId
telemetry.macMachineId
telemetry.devDeviceId
telemetry.sqmId
Kullanım Kılavuzu:
1. Otomatik Kurulum:
Windows: PowerShell'i yönetici olarak çalıştırın ve şu komutu çalıştırın:
powershell
Kodu kopyala
irm https://raw.githubusercontent.com/yuaotian/go-cursor-help/master/scripts/install.ps1 | iex
Linux/macOS:
Terminali açın ve şu komutu çalıştırın:
bash
Kodu kopyala
curl -fsSL https://raw.githubusercontent.com/yuaotian/go-cursor-help/master/scripts/install.sh | sudo bash
2. Manuel Kurulum (Otomatik Yöntem Başarısız Olursa):
Dosya Konumu:
Windows: %APPDATA%\Cursor\User\globalStorage\storage.json
macOS: ~/Library/Application Support/Cursor/User/globalStorage/storage.json
Linux: ~/.config/Cursor/User/globalStorage/storage.json
UUID Alanlarını Değiştirin:
storage.json dosyasını bir metin editörü ile açın ve ilgili alanlara yeni UUID'ler atayın.
Nasıl Çalışır?
Adım Adım Rehberlik:
Program her işlemde kullanıcıya açıklamalar sunar.

Hata Durumlarında Alternatifler:
Otomatik işlem başarısız olduğunda manuel çözüm yolları sağlar.

Geliştirici Dostu:
Açık kaynak kodlu ve esnek yapıya sahiptir.

Bu araç, Cursor deneme sürecini sıfırlamak isteyenler için ideal bir çözüm sunar.
Sorularınız veya katkılarınız için lütfen bu repo üzerinden iletişime geçin! veya kaldırılması için talep edin! 🌟
