import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Original length: {len(html)}")
changes = 0

# ============================================================
# FIX 1: PROFILE CARD — Add photo upload button
# ============================================================
old_profile_card = '''<!-- Profile Card -->
            <div
                class="bg-gradient-to-br from-brand-500 to-brand-600 rounded-3xl p-8 text-center text-white shadow-lg mb-6 relative overflow-hidden">
                <div class="absolute -right-10 -top-10 w-40 h-40 bg-white opacity-10 rounded-full blur-2xl"></div>
                <div class="relative z-10">
                    <div class="w-24 h-24 mx-auto mb-4 rounded-full bg-white/20 p-1 overflow-hidden">
                        <img id="profileAvatar" src="https://api.dicebear.com/7.x/notionists/svg?seed=User"
                            alt="Profile" class="w-full h-full rounded-full bg-white object-cover">
                    </div>
                    <h3 class="font-bold text-xl mb-1" id="profileName">User</h3>
                    <p class="text-sm text-blue-100 mb-4" id="profileEmail">user@smartmoney.app</p>
                    <button onclick="editProfile()"
                        class="px-6 py-2 bg-white/20 hover:bg-white/30 rounded-full text-sm font-medium transition">
                        <i class="fa-solid fa-pen mr-2"></i>Edit Profil
                    </button>
                </div>
            </div>'''

new_profile_card = '''<!-- Profile Card -->
            <div
                class="bg-gradient-to-br from-brand-500 to-brand-600 rounded-3xl p-8 text-center text-white shadow-lg mb-6 relative overflow-hidden">
                <div class="absolute -right-10 -top-10 w-40 h-40 bg-white opacity-10 rounded-full blur-2xl"></div>
                <div class="relative z-10">
                    <!-- Avatar + Upload -->
                    <div class="relative w-24 h-24 mx-auto mb-4 group cursor-pointer" onclick="document.getElementById('avatarUpload').click()">
                        <div class="w-24 h-24 rounded-full bg-white/20 p-1 overflow-hidden">
                            <img id="profileAvatar" src="https://api.dicebear.com/7.x/notionists/svg?seed=User"
                                alt="Profile" class="w-full h-full rounded-full bg-white object-cover">
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center rounded-full bg-black/40 opacity-0 group-hover:opacity-100 transition">
                            <i class="fa-solid fa-camera text-white text-lg"></i>
                        </div>
                        <div class="absolute -bottom-1 -right-1 w-7 h-7 bg-white rounded-full flex items-center justify-center shadow-md">
                            <i class="fa-solid fa-camera text-brand-600 text-xs"></i>
                        </div>
                    </div>
                    <!-- Hidden file input -->
                    <input type="file" id="avatarUpload" accept="image/*" class="hidden" onchange="uploadProfilePhoto(this)">
                    <h3 class="font-bold text-xl mb-1" id="profileName">User</h3>
                    <p class="text-sm text-blue-100 mb-4" id="profileEmail">user@smartmoney.app</p>
                    <div class="flex justify-center gap-3 flex-wrap">
                        <button onclick="editProfile()"
                            class="px-5 py-2 bg-white/20 hover:bg-white/30 rounded-full text-sm font-medium transition">
                            <i class="fa-solid fa-pen mr-2"></i>Edit Profil
                        </button>
                        <button onclick="document.getElementById('avatarUpload').click()"
                            class="px-5 py-2 bg-white/20 hover:bg-white/30 rounded-full text-sm font-medium transition">
                            <i class="fa-solid fa-camera mr-2"></i>Ganti Foto
                        </button>
                    </div>
                </div>
            </div>'''

if old_profile_card in html:
    html = html.replace(old_profile_card, new_profile_card, 1)
    changes += 1
    print("FIX 1 DONE: Profile card updated with photo upload")
else:
    print("FIX 1 SKIP: Profile card not found (may already be changed)")

# ============================================================
# FIX 2: LANGUAGE SELECT — Add id and onchange handler
# ============================================================
old_lang_select = '''<select
                            class="bg-transparent text-right outline-none text-sm font-bold text-brand-600 dark:text-brand-400 cursor-pointer">
                            <option value="id">Indonesia</option>
                            <option value="en">English</option>
                        </select>'''

new_lang_select = '''<select id="langSelect" onchange="changeLanguage(this.value)"
                            class="bg-transparent text-right outline-none text-sm font-bold text-brand-600 dark:text-brand-400 cursor-pointer">
                            <option value="id">Indonesia</option>
                            <option value="en">English</option>
                        </select>'''

if old_lang_select in html:
    html = html.replace(old_lang_select, new_lang_select, 1)
    changes += 1
    print("FIX 2 DONE: Language select fixed with id and onchange")
else:
    print("FIX 2 SKIP: Language select not found")

# ============================================================
# FIX 3: CONTACT DEVELOPER — Replace alert with proper modal
# ============================================================
old_contact_btn_section = '''<!-- Contact Developer -->
                    <div class="p-5 hover:bg-slate-50 dark:hover:bg-slate-700/50 transition">
                        <button onclick="contactDeveloper()" class="w-full flex items-center gap-4 text-left">
                            <div
                                class="w-10 h-10 rounded-full bg-brand-100 dark:bg-brand-900/30 text-brand-600 dark:text-brand-400 flex items-center justify-center">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <p class="font-bold text-slate-800 dark:text-white text-sm">Hubungi Pembuat</p>
                                <p class="text-xs text-slate-400">Kirim feedback atau laporan bug</p>
                            </div>
                        </button>
                    </div>'''

new_contact_btn_section = '''<!-- Contact Developer -->
                    <div class="p-5 hover:bg-slate-50 dark:hover:bg-slate-700/50 transition">
                        <button onclick="showContactModal()" class="w-full flex items-center gap-4 text-left">
                            <div
                                class="w-10 h-10 rounded-full bg-brand-100 dark:bg-brand-900/30 text-brand-600 dark:text-brand-400 flex items-center justify-center">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <p class="font-bold text-slate-800 dark:text-white text-sm">Hubungi Pembuat</p>
                                <p class="text-xs text-slate-400">Email & WhatsApp Mas Alfian</p>
                            </div>
                        </button>
                    </div>'''

if old_contact_btn_section in html:
    html = html.replace(old_contact_btn_section, new_contact_btn_section, 1)
    changes += 1
    print("FIX 3 DONE: Contact button updated")
else:
    print("FIX 3 SKIP: Contact button section not found")

# ============================================================
# FIX 3b: Add Contact Modal HTML (before </body>)
# ============================================================
contact_modal_html = '''
        <!-- Modal: Hubungi Pembuat -->
        <div id="contactModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 hidden">
            <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" onclick="closeContactModal()"></div>
            <div class="relative bg-white dark:bg-dark-800 rounded-3xl shadow-2xl w-full max-w-sm p-8 z-10 animate-fade-in">
                <div class="text-center mb-6">
                    <div class="w-16 h-16 bg-gradient-to-br from-brand-500 to-brand-600 rounded-2xl flex items-center justify-center text-white text-2xl mx-auto mb-4 shadow-lg">
                        <i class="fa-solid fa-headset"></i>
                    </div>
                    <h3 class="text-xl font-bold text-slate-900 dark:text-white">Hubungi Pembuat</h3>
                    <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Smart Money dibuat oleh <strong>Mas Alfian</strong></p>
                </div>

                <!-- Email -->
                <a href="mailto:alfiangopoh09@gmail.com?subject=Feedback%20Smart%20Money"
                    class="flex items-center gap-4 p-4 rounded-2xl border border-slate-100 dark:border-slate-700 hover:bg-brand-50 dark:hover:bg-brand-900/20 transition mb-3 group">
                    <div class="w-11 h-11 rounded-full bg-red-100 dark:bg-red-900/30 flex items-center justify-center text-red-500 flex-shrink-0 group-hover:scale-110 transition">
                        <i class="fa-solid fa-envelope text-lg"></i>
                    </div>
                    <div>
                        <p class="font-bold text-slate-800 dark:text-white text-sm">Email</p>
                        <p class="text-xs text-slate-500 dark:text-slate-400">alfiangopoh09@gmail.com</p>
                    </div>
                    <i class="fa-solid fa-arrow-right ml-auto text-slate-400 group-hover:text-brand-500 transition"></i>
                </a>

                <!-- WhatsApp -->
                <a href="https://wa.me/6285732491409?text=Halo%20Mas%20Alfian%2C%20saya%20ingin%20memberikan%20feedback%20terkait%20aplikasi%20Smart%20Money."
                    target="_blank" rel="noopener"
                    class="flex items-center gap-4 p-4 rounded-2xl border border-slate-100 dark:border-slate-700 hover:bg-green-50 dark:hover:bg-green-900/20 transition mb-6 group">
                    <div class="w-11 h-11 rounded-full bg-green-100 dark:bg-green-900/30 flex items-center justify-center text-green-500 flex-shrink-0 group-hover:scale-110 transition">
                        <i class="fa-brands fa-whatsapp text-lg"></i>
                    </div>
                    <div>
                        <p class="font-bold text-slate-800 dark:text-white text-sm">WhatsApp</p>
                        <p class="text-xs text-slate-500 dark:text-slate-400">085732491409</p>
                    </div>
                    <i class="fa-solid fa-arrow-right ml-auto text-slate-400 group-hover:text-green-500 transition"></i>
                </a>

                <button onclick="closeContactModal()"
                    class="w-full py-3 bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 rounded-2xl text-sm font-semibold text-slate-700 dark:text-slate-200 transition">
                    Tutup
                </button>
            </div>
        </div>

'''

if 'id="contactModal"' not in html:
    # Insert before </body>
    html = html.replace('</body>', contact_modal_html + '</body>', 1)
    changes += 1
    print("FIX 3b DONE: Contact modal HTML added")
else:
    print("FIX 3b SKIP: Contact modal already exists")

# ============================================================
# FIX 4: Replace all JS functions at once
# ============================================================

# --- 4a: contactDeveloper -> showContactModal + closeContactModal
old_contact_func = '''function contactDeveloper() {
            const message = prompt('Apa yang ingin Anda sampaikan? (feedback/bug/saran):');
            if (message && message.trim()) {
                alert('✉️ Terima kasih atas feedback Anda!\\n\\n"' + message + '"\\n\\nSilakan kirim ke:\\n📧 Email: alfian@smartmoney.app\\n💬 WhatsApp: +62-xxx-xxx-xxxx');
            }
        }'''

new_contact_func = '''function contactDeveloper() { showContactModal(); }

        function showContactModal() {
            document.getElementById('contactModal').classList.remove('hidden');
        }

        function closeContactModal() {
            document.getElementById('contactModal').classList.add('hidden');
        }'''

if old_contact_func in html:
    html = html.replace(old_contact_func, new_contact_func, 1)
    changes += 1
    print("FIX 4a DONE: contactDeveloper replaced with modal functions")
else:
    # Try partial match
    old_part = "function contactDeveloper() {"
    if old_part in html:
        idx = html.index(old_part)
        end_idx = html.index("}", idx) + 1
        old_block = html[idx:end_idx]
        html = html.replace(old_block, new_contact_func, 1)
        changes += 1
        print("FIX 4a DONE (partial): contactDeveloper replaced")
    else:
        print("FIX 4a SKIP: contactDeveloper not found")

# --- 4b: editProfile — also handle email editing
old_edit_profile = '''function editProfile() {
            const newName = prompt('Nama baru:', currentUser);
            if (newName && newName.trim()) {
                currentUser = newName.trim();
                localStorage.setItem('userName', currentUser);
                document.getElementById('profileName').textContent = currentUser;
            }
        }'''

new_edit_profile = '''function editProfile() {
            const newName = prompt('Nama Anda:', currentUser);
            if (newName && newName.trim()) {
                currentUser = newName.trim();
                localStorage.setItem('userName', currentUser);
                document.getElementById('profileName').textContent = currentUser;
            }
            const newEmail = prompt('Email Anda:', localStorage.getItem('userEmail') || 'user@smartmoney.app');
            if (newEmail && newEmail.trim()) {
                localStorage.setItem('userEmail', newEmail.trim());
                const emailEl = document.getElementById('profileEmail');
                if (emailEl) emailEl.textContent = newEmail.trim();
            }
        }

        function uploadProfilePhoto(input) {
            const file = input.files[0];
            if (!file) return;
            if (file.size > 5 * 1024 * 1024) {
                alert('Ukuran foto maksimal 5 MB. Silakan pilih foto yang lebih kecil.');
                return;
            }
            const reader = new FileReader();
            reader.onload = function(e) {
                const base64 = e.target.result;
                localStorage.setItem('userAvatar', base64);
                const avatarEl = document.getElementById('profileAvatar');
                if (avatarEl) avatarEl.src = base64;
            };
            reader.readAsDataURL(file);
        }

        function loadProfilePhoto() {
            const saved = localStorage.getItem('userAvatar');
            const avatarEl = document.getElementById('profileAvatar');
            if (saved && avatarEl) avatarEl.src = saved;
            const savedEmail = localStorage.getItem('userEmail');
            const emailEl = document.getElementById('profileEmail');
            if (savedEmail && emailEl) emailEl.textContent = savedEmail;
        }'''

if old_edit_profile in html:
    html = html.replace(old_edit_profile, new_edit_profile, 1)
    changes += 1
    print("FIX 4b DONE: editProfile + uploadProfilePhoto + loadProfilePhoto added")
else:
    print("FIX 4b SKIP: editProfile not found as expected")

# --- 4c: Language change function + translations
lang_func = '''
        // ============================================
        // BAHASA / LANGUAGE SWITCHER
        // ============================================
        const appTranslations = {
            id: {
                nav_home: 'Beranda', nav_transactions: 'Transaksi', nav_reports: 'Laporan', nav_settings: 'Pengaturan',
                settings_title: 'Pengaturan', settings_subtitle: 'Kelola akun dan preferensi aplikasi',
                settings_dark_mode: 'Mode Gelap', settings_dark_mode_sub: 'Tema tampilan',
                settings_language: 'Bahasa', settings_language_sub: 'ID / EN',
                settings_delete_data: 'Hapus Semua Data', settings_delete_data_sub: 'Reset aplikasi',
                settings_contact: 'Hubungi Pembuat', settings_contact_sub: 'Email & WhatsApp Mas Alfian',
                greeting: 'Selamat datang',
                balance_label: 'Saldo Saat Ini',
                income_label: 'Pemasukan',
                expense_label: 'Pengeluaran',
            },
            en: {
                nav_home: 'Home', nav_transactions: 'Transactions', nav_reports: 'Reports', nav_settings: 'Settings',
                settings_title: 'Settings', settings_subtitle: 'Manage your account and app preferences',
                settings_dark_mode: 'Dark Mode', settings_dark_mode_sub: 'Display theme',
                settings_language: 'Language', settings_language_sub: 'ID / EN',
                settings_delete_data: 'Delete All Data', settings_delete_data_sub: 'Reset application',
                settings_contact: 'Contact Developer', settings_contact_sub: 'Email & WhatsApp Mas Alfian',
                greeting: 'Welcome',
                balance_label: 'Current Balance',
                income_label: 'Income',
                expense_label: 'Expenses',
            }
        };

        let currentLang = localStorage.getItem('appLang') || 'id';

        function changeLanguage(lang) {
            if (!appTranslations[lang]) return;
            currentLang = lang;
            localStorage.setItem('appLang', lang);
            applyLanguage(lang);
        }

        function applyLanguage(lang) {
            const t = appTranslations[lang] || appTranslations['id'];
            // Nav labels
            const navMap = {
                'nav-label-home': t.nav_home,
                'nav-label-transactions': t.nav_transactions,
                'nav-label-reports': t.nav_reports,
                'nav-label-settings': t.nav_settings,
            };
            Object.entries(navMap).forEach(([id, text]) => {
                const el = document.getElementById(id);
                if (el) el.textContent = text;
            });
            // Settings page
            const setTitle = document.querySelector('#view-settings h2');
            if (setTitle) setTitle.textContent = t.settings_title;
            const setSubtitle = document.querySelector('#view-settings > p');
            if (setSubtitle) setSubtitle.textContent = t.settings_subtitle;
            // Update select value
            const sel = document.getElementById('langSelect');
            if (sel) sel.value = lang;
        }

        function initLanguage() {
            const saved = localStorage.getItem('appLang') || 'id';
            currentLang = saved;
            const sel = document.getElementById('langSelect');
            if (sel) sel.value = saved;
            if (saved !== 'id') applyLanguage(saved);
        }
'''

# Insert language function before the closing of the script tag (before logout or clearAllData)
insert_before = 'function logout()'
if lang_func not in html and insert_before in html:
    html = html.replace(insert_before, lang_func + '\n        function logout()', 1)
    changes += 1
    print("FIX 4c DONE: Language functions added")
elif lang_func not in html:
    print("FIX 4c SKIP: Could not find insertion point for language functions")
else:
    print("FIX 4c SKIP: Language functions already exist")

# ============================================================
# FIX 5: Add nav label IDs for language switching
# ============================================================
# Try to add IDs to bottom nav labels if they don't exist
nav_fixes = [
    ('fa-house</i>Beranda', 'fa-house</i><span id="nav-label-home">Beranda</span>'),
    ('fa-list</i>Transaksi', 'fa-list</i><span id="nav-label-transactions">Transaksi</span>'),
    ('fa-chart-line</i>Laporan', 'fa-chart-line</i><span id="nav-label-reports">Laporan</span>'),
    ('fa-gear</i>Pengaturan', 'fa-gear</i><span id="nav-label-settings">Pengaturan</span>'),
]
for old, new in nav_fixes:
    if old in html and new not in html:
        html = html.replace(old, new, 1)
        changes += 1
        print(f"FIX 5 DONE: Nav label ID added for {old[:20]}")

# ============================================================
# FIX 6: CSV Export — cleaner, proper formatting
# ============================================================
old_csv_func_start = 'function exportToCSV() {'
old_csv_func_end = '// ===========================================\n        // EKSPOR KE PDF'

old_csv_start_idx = html.find(old_csv_func_start)
old_csv_end_idx = html.find(old_csv_func_end, old_csv_start_idx)

if old_csv_start_idx != -1 and old_csv_end_idx != -1:
    old_csv_block = html[old_csv_start_idx:old_csv_end_idx]
    
    new_csv_block = r"""function exportToCSV() {
            const data = getFilteredReportData();
            const { filtered, income, expense, balance, periodLabel, accountFilter, categoryFilter } = data;

            if (filtered.length === 0) {
                alert('⚠️ Tidak ada data untuk diekspor!');
                return;
            }

            const now = new Date();
            const printDateStr = now.toLocaleDateString('id-ID', { day: '2-digit', month: 'long', year: 'numeric' })
                + ' ' + now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });

            // Format angka Rupiah (tanpa simbol Rp agar Excel bisa mengenali sebagai angka)
            function fmtNum(n) { return Number(n).toLocaleString('id-ID'); }

            // Escape nilai CSV: bungkus dengan kutip, ganda-kan kutip di dalam
            function esc(val) {
                if (val === null || val === undefined) return '""';
                const s = String(val).replace(/"/g, '""');
                return '"' + s + '"';
            }

            const sep = ',';
            const lines = [];

            // ── HEADER LAPORAN ──────────────────────────────
            lines.push([esc('SMART MONEY - LAPORAN KEUANGAN'), '', '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Waktu Ekspor'), esc(printDateStr), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Pengguna'), esc(currentUser || 'User'), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Periode'), esc(periodLabel), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Akun'), esc(accountFilter || 'Semua Akun'), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Kategori'), esc(categoryFilter || 'Semua Kategori'), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Jumlah Transaksi'), esc(filtered.length + ' transaksi'), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push(''); // baris kosong pemisah

            // ── RINGKASAN KEUANGAN ──────────────────────────
            lines.push([esc('RINGKASAN KEUANGAN'), '', '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Total Pemasukan'), esc('Rp ' + fmtNum(income)), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Total Pengeluaran'), esc('Rp ' + fmtNum(expense)), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push([esc('Saldo Bersih'), esc('Rp ' + fmtNum(balance)), '', '', '', '', '', '', '', '', ''].join(sep));
            lines.push(''); // baris kosong pemisah

            // ── HEADER TABEL TRANSAKSI ──────────────────────
            const headers = ['No', 'Tanggal', 'Waktu', 'Keterangan', 'Kategori', 'Akun', 'Tipe', 'Pemasukan (Rp)', 'Pengeluaran (Rp)', 'Nominal (Rp)', 'Arus Kas'];
            lines.push(headers.map(esc).join(sep));

            // ── BARIS DATA TRANSAKSI ────────────────────────
            filtered.forEach((t, idx) => {
                const dt = formatTransactionDate(t.date);
                const isInc = t.type === 'income';
                const row = [
                    idx + 1,
                    dt.date || '-',
                    dt.time || '-',
                    t.description || '-',
                    t.category || '-',
                    t.account || '-',
                    isInc ? 'Pemasukan' : 'Pengeluaran',
                    isInc ? fmtNum(t.amount) : '0',
                    !isInc ? fmtNum(t.amount) : '0',
                    fmtNum(t.amount),
                    isInc ? '+ Masuk' : '- Keluar'
                ];
                lines.push(row.map(esc).join(sep));
            });

            // ── BARIS TOTAL ─────────────────────────────────
            const totalRow = [
                'TOTAL', '', '', filtered.length + ' Transaksi', '', '', '',
                fmtNum(income), fmtNum(expense), fmtNum(balance),
                balance >= 0 ? 'SURPLUS' : 'DEFISIT'
            ];
            lines.push(totalRow.map(esc).join(sep));

            // ── BUILD & DOWNLOAD ────────────────────────────
            const csvContent = '\uFEFF' + lines.join('\r\n');
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'SmartMoney_Laporan_' + periodLabel.replace(/\s+/g, '_') + '_' + Date.now() + '.csv';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            showExportToast('\u2705 Laporan CSV berhasil diunduh!');
        }

        """
    
    html = html[:old_csv_start_idx] + new_csv_block + html[old_csv_end_idx:]
    changes += 1
    print("FIX 6 DONE: CSV export function replaced")
else:
    print(f"FIX 6 SKIP: CSV function markers not found (start={old_csv_start_idx}, end={old_csv_end_idx})")

# ============================================================
# FIX 7: Call loadProfilePhoto + initLanguage on app init
# ============================================================
old_init_call = 'loadTransactions();'
new_init_call = 'loadTransactions();\n            loadProfilePhoto();\n            initLanguage();'

if old_init_call in html and 'loadProfilePhoto()' not in html:
    html = html.replace(old_init_call, new_init_call, 1)
    changes += 1
    print("FIX 7 DONE: loadProfilePhoto + initLanguage called on init")
elif 'loadProfilePhoto()' in html:
    print("FIX 7 SKIP: loadProfilePhoto already in init")
else:
    print("FIX 7 SKIP: loadTransactions() init call not found")

print(f"\nTotal changes: {changes}")
print(f"New length: {len(html)}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: All fixes written to index.html!")
