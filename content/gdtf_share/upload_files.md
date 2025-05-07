---
title: "Upload Files"
description: "GDTF documentation"
lead: ""
date: 2020-10-06T08:48:23+00:00
lastmod: 2020-10-06T08:48:23+00:00
draft: false
images: []
weight: 80
---
Clicking the {{% image_inline src="../media/Icon_Upload.png" alt="" %}}  icon
in the title bar opens the **Upload** page.

**Hint:**  You can also upload your GDTF file by Drag & Drop on the upload
page.

There is one button called Choose a file. Clicking it opens a file browser on
the computer where the desired GDTF file can be selected. You can close the
upload page at any time by clicking the {{% image_inline src="../media/Icon_Close.png" alt="" %}}  in the upper right corner.

{{% figure src="../media/Window_Upload2.png" caption="Select file for upload" %}}

When the file is selected a new button appears. It is called Proceed. This is
an example with a gdtf file:

{{% figure src="../media/Window_upload_with_file_selected.png" caption="" %}}

Click the Proceed button to upload the file. A progress will be shown.

{{% figure src="../media/Window_upload_progress.png" caption="Upload progress" %}}

When the file is uploaded, it is analyzed for manufacturer name, device name
and so on. The Share first tries to match an existing manufacturer. If needed,
manufacturer can be changed. The Clear file button clears all the info and
cancels the upload.

{{% figure src="../media/Window_Upload_select_device_name.png" caption="Device name dialog" %}}

Then the name of the device is checked and if needed it can be changed.

{{% figure src="../media/Window_Upload_select_manufacturer.png" caption="Select manufacturer dialog" %}}

Next you need to add a Revision name for the uploaded file and also a Release
status. The revision text can be up to 90 characters. For example, if it is the
first version of the fixture, it could be called "First version". If there is
something that has been changed in the fixture file, then it can be a good idea
to write what was changed.

The Revision status is by default set to WIP (Work In Progress), allowing you
to save your work without publishing it yet. If you are ready to publish the
file, you can set the Release status to Release. The Release status can also be
changed later from inside the GDTF Share.

{{% figure src="../media/Window_upload_revision_release_status.png" caption="Revision and Release status" %}}

Clicking the Upload button uploads the file to the library and you can choose
the Back to the Share button to close this dialog and go back to the share or
click Upload another file to continue by uploading another file.

{{% figure src="../media/Window_upload_file_uploaded.png" caption="File uploaded" %}}
