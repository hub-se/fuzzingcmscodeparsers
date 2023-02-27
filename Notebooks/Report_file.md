## Errors for code: vasp

| Key | Description |
| :--- | :--- |
|**ID**| vasp:critical:0|
|**Error class**| Critical|
|**Comment**| Memory error from reshaping empty array of DOS values. May produce huge ArchiveEntry()s if memory error is not explicitly raised.|
|**Example file**| vasp/run-16/file000095
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|L_aTDm3nu6NUmMwUE3kwMP3blXkB|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:critical:1|
|**Error class**| Critical|
|**Comment**| Memory error from attempting to serialize too large ArchiveEntry.|
|**Example file**| vasp/run-0/file000084
|**Details**| |
|**additional_exceptions**|['    json.dump(entry_archive.m_to_dict(), sys.stdout, indent=2)\n', '    return serialize(value)\n', '    return value.tolist()\n', 'MemoryError\n']|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:critical:2|
|**Error class**| Critical|
|**Comment**| Memory error from generating a huge array of ISPIN * [efermi]. Because ISPIN can be huge, this is unsafe.|
|**Example file**| vasp/run-0/file000084
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|su00nKJydlxcNins1Kj5BpdfdE6e|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:logical:0|
|**Error class**| Logical|
|**Comment**| Uncatchable exception in SPGLIB.|
|**Example file**| vasp/run-14/file000095
|**Details**| |
|**additional_exceptions**|["    'Spglib error when finding symmetry dataset.')\n"]|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:logical:1|
|**Error class**| Logical|
|**Comment**| Random string in atomtypes breaks retrieval of values. Therefore, the default value, for atomtype.element is used, which is an (unhashable) list, raising a TypeError.|
|**Example file**| vasp/run-4/file000059
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|1Tx__spX2-YFYzHb0n0GYOR5g0nr|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:logical:2|
|**Error class**| Logical|
|**Comment**| Uncaught exception in workflow normalizer: tries to read incar (part of input file), which is not present, and default value is None, which can not be processed in the following.|
|**Example file**| vasp/run-4/file000059
|**Details**| |
|**additional_exceptions**|["    nsw = incar.get('NSW')\n", "AttributeError: 'NoneType' object has no attribute 'get'\n"]|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:logical:3|
|**Error class**| Logical|
|**Comment**| Memory error from attempting to convert eigenvalues to different unit, conversion was not done inplace.|
|**Example file**| vasp/run-28/file000028
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|-Nwm0XRg9cFl_Nz5Tch5MCJnPwvl|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:0|
|**Error class**| Semantic|
|**Comment**| The parsing of eigenvalues relies on a reshape of the values read from file with the number of spins, the number of eigenvalues, the number of k-points and the number of bands. If these numnbers are not consistent, the reshaping may fail, producing this error.|
|**Example file**| vasp/run-0/file000001
|**Details**| |
|**message**|Error reading eigenvalues|
|**error_type**|ERROR|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:1|
|**Error class**| Semantic|
|**Comment**| The parsing of the total DOS relies on the reshaping of the dos w.r.t. their length, and the number of spins. If the number of spins is invalid, this will fail. Another reason is that the total dos fields can be empty.|
|**Example file**| vasp/run-0/file000001
|**Details**| |
|**message**|Error reading total dos.|
|**error_type**|ERROR|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:2|
|**Error class**| Semantic|
|**Comment**| In the VASP file, the atomic positions are defined at a different place than the species. If the number of positions does not agree with the number of species, this error is raised.|
|**Example file**| vasp/run-0/file000001
|**Details**| |
|**message**|len of atom position does not match number of atoms|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:3|
|**Error class**| Semantic|
|**Comment**| Error related to reshaping of kpoints. The value 'divisions' was parsed as a negative value, which is passed directly to reshape, resulting in two negative vales for the shapes in np.reshape, which raises an error.|
|**Example file**| vasp/run-0/file000002
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|1OV1pJegrYDIjH_wqhGZTuhgQeWf|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:4|
|**Error class**| Semantic|
|**Comment**| The value 'divisions' was fuzzed as '0', is directly from file and thus introduces a ZeroDivisionError.|
|**Example file**| vasp/run-0/file000003
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|TAJ-ueqNJyPjsShsR6kVV-5LD2ih|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:5|
|**Error class**| Semantic|
|**Comment**| Unit cell vector is null vector, which raises an assertion.|
|**Example file**| vasp/run-0/file000036
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|57YamOvgvaRUgjZNc_PlrnsfHPjH|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:6|
|**Error class**| Semantic|
|**Comment**| Unphysical atom positions can not be processed.|
|**Example file**| vasp/run-0/file000060
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Op54Up8lxWBrBHUHMym4gvsuXShR|
|**nomad.cli.error**|Singular matrix|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:7|
|**Error class**| Semantic|
|**Comment**| Memory error in matid find_mic: unphysical system|
|**Example file**| vasp/run-0/file000082
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|qkMjKLtYkj4WgMn3IIU7mLDT7Y51|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:8|
|**Error class**| Semantic|
|**Comment**| Eigenvalue array is empty, but parser attempts to find np.amin() of it.|
|**Example file**| vasp/run-3/file000028
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|YgyyskAhD9fqWur0Avq-nWhA1-SJ|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:9|
|**Error class**| Semantic|
|**Comment**| Memory error in matid find_mic|
|**Example file**| vasp/run-3/file000069
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:10|
|**Error class**| Semantic|
|**Comment**| Empty positions vector forces matid periodicfinder to fail.|
|**Example file**| vasp/run-20/file000067
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|h2cL8znAvo-Q4yWPVSNWBZ69OENP|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:semantic:11|
|**Error class**| Semantic|
|**Comment**| Error reading partial dos, most likely related to semantic mismatch in file.|
|**Example file**| vasp/run-0/file000030
|**Details**| |
|**message**|Error reading partial dos.|
|**error_type**|ERROR|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:syntactic:0|
|**Error class**| Syntactic|
|**Comment**| In some cases, atom positions are an empty array. In that case, the conversion of the positons to a pint Quantity fails, because the (empty) postions are multiplied by a non-empty cell matrix.|
|**Example file**| vasp/run-0/file000012
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|BfbTfhKsTA5SBnJwv6lKOVDowmtQ|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:syntactic:1|
|**Error class**| Syntactic|
|**Comment**| Timing information in the header of the VASP mainfile was fuzzed with random string, which can not be interpreted by datetime.|
|**Example file**| vasp/run-0/file000020
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|EaKv-6irFJ0BnhJ7SmQ2qNZSPaEp|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:syntactic:2|
|**Error class**| Syntactic|
|**Comment**| Date was fuzzed as random string, which can not be iterpreted as a date.|
|**Example file**| vasp/run-0/file000057
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|OoSk1nxLMIbAP3ZwjqAE0MZM6Klk|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:syntactic:3|
|**Error class**| Syntactic|
|**Comment**| Atom type fuzzed as random string breaks atom label detection.|
|**Example file**| vasp/run-0/file000010
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|GNAbslrIMxKV1-KcY655PssnNrUV|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:syntactic:4|
|**Error class**| Syntactic|
|**Comment**| For some reason, some value in the pseodopotential description is interpreted as a float, but is supposed to be a string. Deeper reason cannot be estimated.|
|**Example file**| vasp/run-12/file000051
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|WOHT6kai_wDOJnd-K95qtrsgYYTR|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:syntactic:5|
|**Error class**| Syntactic|
|**Comment**| k-point generation schema fuzzed as random string|
|**Example file**| vasp/run-0/file000018
|**Details**| |
|**message**|Error setting metainfo|
|**error_type**|WARNING|
|**nomad.cli.data**|{'key': 'x_vasp_k_points_generation_method'}|
|**nomad.cli.parser**|parsers/vasp|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:downstream:0|
|**Error class**| Downstream|
|**Comment**| If a system could not be parsed, the metadata is not populated.|
|**Example file**| vasp/run-0/file000012
|**Details**| |
|**message**|system has neither atom species nor labels|
|**error_type**|WARNING|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:downstream:1|
|**Error class**| Downstream|
|**Comment**| With a non-existing section system, the optimade normalizer was failing. However, this appears to be fixed in NOMAD branch master already.|
|**Example file**| vasp/run-0/file000012
|**Details**| |
|**message**|could not acquire optimade data|
|**error_type**|WARNING|
|**exception_hash**|sO_OioUn6QJmanbzDfhEnRmCzvSv|
|**nomad.cli.normalizer**|OptimadeNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:downstream:2|
|**Error class**| Downstream|
|**Comment**| If the parsing of the system fails, the normalizer has no data to work on.|
|**Example file**| vasp/run-0/file000020
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:downstream:3|
|**Error class**| Downstream|
|**Comment**| If the parsing of the system fails, the normalizer has no data to work on.|
|**Example file**| vasp/run-0/file000020
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|OptimadeNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:downstream:4|
|**Error class**| Downstream|
|**Comment**| Uncaught exception in workflow normalizer: Dimension of forces appears to be wrong. TODO Report!|
|**Example file**| vasp/run-0/file000055
|**Details**| |
|**additional_exceptions**|['    max_force = np.max(np.linalg.norm(forces, axis=1))\n', '    return sqrt(add.reduce(s, axis=axis, keepdims=keepdims))\n', 'numpy.AxisError: axis 1 is out of bounds for array of dimension 1\n']|
| | |
|**----**|**----**|
| | |
|**ID**| vasp:downstream:5|
|**Error class**| Downstream|
|**Comment**| Uncatchable error in SPGLIB.|
|**Example file**| vasp/run-14/file000095
|**Details**| |
|**message**|failed to process encyclopedia data due to an unhandlable exception|
|**error_type**|ERROR|
|**nomad.cli.enc_status**|failure|
|**nomad.cli.normalizer**|EncyclopediaNormalizer|
| | |
|**----**|**----**|
| | |

## Errors for code: exciting

| Key | Description |
| :--- | :--- |
|**ID**| exciting:logical:0|
|**Error class**| Logical|
|**Comment**| If the force components in the final iteration have only one entry, this exception is raised.|
|**Example file**| exciting/run-0/file000042
|**Details**| |
|**additional_exceptions**|['    max_force = np.max(np.linalg.norm(forces, axis=1))\n', 'numpy.AxisError: axis 1 is out of bounds for array of dimension 1\n']|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:logical:1|
|**Error class**| Logical|
|**Comment**| Failure in Spglib, which is not caught. Can be related to an unphysical system.|
|**Example file**| exciting/run-4/file000053
|**Details**| |
|**additional_exceptions**|["    'Spglib error when finding symmetry dataset.')\n", 'matid.exceptions.CellNormalizationError: Spglib error when finding symmetry dataset.\n']|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:0|
|**Error class**| Semantic|
|**Comment**| Semantic error - the numbers of atoms do not match, so the normalizer raises an error.|
|**Example file**| exciting/run-0/file000015
|**Details**| |
|**message**|len of atom position does not match number of atoms|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:1|
|**Error class**| Semantic|
|**Comment**| This assertion is (correctly) triggered if one of the cell vectors has length 0. However, is does catch situations where the cell vectors are identical.|
|**Example file**| exciting/run-0/file000045
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|57YamOvgvaRUgjZNc_PlrnsfHPjH|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:2|
|**Error class**| Semantic|
|**Comment**| Normalizer error, which can occur if the atom positions are semantically wrong.|
|**Example file**| exciting/run-1/file000016
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Op54Up8lxWBrBHUHMym4gvsuXShR|
|**nomad.cli.error**|Singular matrix|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:3|
|**Error class**| Semantic|
|**Comment**| The unit cell that is to be processed is too big to be processed. Also crashes ASE plotting routines.|
|**Example file**| exciting/run-1/file000035
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**|array is too big; `arr.size * arr.dtype.itemsize` is larger than the maximum possible size.|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:4|
|**Error class**| Semantic|
|**Comment**| The unit cell is too big to be processed. Also crashes ASE plotting routines.|
|**Example file**| exciting/run-3/file000009
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|qkMjKLtYkj4WgMn3IIU7mLDT7Y51|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:5|
|**Error class**| Semantic|
|**Comment**| Unit cell is too big to be processed. Crashes ASE plotting.|
|**Example file**| exciting/run-8/file000015
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|DwwGroUpthlSGBt9iVsGOsoF_kIJ|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:6|
|**Error class**| Semantic|
|**Comment**| Unit cell is too big to be processed. Crashes ASE plotting.|
|**Example file**| exciting/run-9/file000044
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|hnU7FBaHMUIs-cXYbp4zgZuYCYSR|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:semantic:7|
|**Error class**| Semantic|
|**Comment**| Normalizing error because of unphysical system.|
|**Example file**| exciting/run-2/file000067
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|2n04qJKFWHYLrisjLf9jghaXUogz|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:syntactic:0|
|**Error class**| Syntactic|
|**Comment**| For an unkown reason, the integer in the file is interpreted as a float, which leads to a collision with the data model. However, the reason why it is interpreted as a float can not be estimated.|
|**Example file**| exciting/run-0/file000028
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|I5vvBLfo0PFtIokjHB08dN4mE0_9|
|**nomad.cli.parser**|parsers/exciting|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:downstream:0|
|**Error class**| Downstream|
|**Comment**| This error is thrown if the parsing does not provide a section_system.|
|**Example file**| exciting/run-0/file000001
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:downstream:1|
|**Error class**| Downstream|
|**Comment**| This error is thrown if the parsing does not provide a section_system.|
|**Example file**| exciting/run-0/file000001
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|OptimadeNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:downstream:2|
|**Error class**| Downstream|
|**Comment**| error message that propagates an uncaught exception|
|**Example file**| exciting/run-4/file000053
|**Details**| |
|**message**|failed to process encyclopedia data due to an unhandlable exception|
|**error_type**|ERROR|
|**nomad.cli.enc_status**|failure|
|**nomad.cli.normalizer**|EncyclopediaNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| exciting:warning:0|
|**Error class**| Warning|
|**Comment**| Unidentified error when trying to set the charge contributions. Regex works, values look reasonable, comparison with successful file did not reveal anything obvious.|
|**Example file**| exciting/run-6/file000008
|**Details**| |
|**message**|Error setting value|
|**error_type**|WARNING|
|**nomad.cli.data**|{'quantity': 'charge_contributions'}|
|**nomad.cli.parser**|parsers/exciting|
| | |
|**----**|**----**|
| | |

## Errors for code: aims

| Key | Description |
| :--- | :--- |
|**ID**| aims:logical:0|
|**Error class**| Logical|
|**Comment**| Error in reshaping kpoints. For some k points, the list of eigenvalues is empty, which leads to the reshape error. Error illustrates logical error, however is raised due to syntactic inaccuracies.|
|**Example file**| aims/run-0/file000070
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|Pxdmz92W21zBRuTq_c8fBfJsttI7|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:logical:1|
|**Error class**| Logical|
|**Comment**| Integer overflow error within matid. Triggered by semantic mismatch.|
|**Example file**| aims/run-10/file000043
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**|negative dimensions are not allowed|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:logical:2|
|**Error class**| Logical|
|**Comment**| Suspected integer overflow in matid.|
|**Example file**| aims/run-4/file000054
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|2n04qJKFWHYLrisjLf9jghaXUogz|
|**nomad.cli.error**|negative dimensions are not allowed|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:logical:3|
|**Error class**| Logical|
|**Comment**| Hard failure of spglib causes unhandlable exception.|
|**Example file**| aims/run-0/file000022
|**Details**| |
|**additional_exceptions**|["    'Spglib error when finding symmetry dataset.')\n", 'matid.exceptions.CellNormalizationError: Spglib error when finding symmetry dataset.\n']|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:0|
|**Error class**| Semantic|
|**Comment**| In these cases, atom species are fuzzed by random special characters, which are not caught by the regex.|
|**Example file**| aims/run-5/file000061
|**Details**| |
|**message**|system has neither atom species nor labels|
|**error_type**|WARNING|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:1|
|**Error class**| Semantic|
|**Comment**| Number of tasks and task assingnment differ, because one of the "hosts" has an empty string as its name. Therefore the counts for both groups are different.|
|**Example file**| aims/run-0/file000002
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|WqVSIaP0tsRJD9h3XLYFCKcjW8Ja|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:2|
|**Error class**| Semantic|
|**Comment**| Assertion triggered by null-vector in unit cell definition.|
|**Example file**| aims/run-0/file000021
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|57YamOvgvaRUgjZNc_PlrnsfHPjH|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:3|
|**Error class**| Semantic|
|**Comment**| Huge unit cell leads to problems in finding the Minimal Image Convention representation.|
|**Example file**| aims/run-0/file000027
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|qkMjKLtYkj4WgMn3IIU7mLDT7Y51|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:4|
|**Error class**| Semantic|
|**Comment**| One atom species is fuzzed by special characters, which break the regex grabbing the species.|
|**Example file**| aims/run-0/file000030
|**Details**| |
|**message**|len of atom position does not match number of atoms|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:5|
|**Error class**| Semantic|
|**Comment**| Unphysical geometry does not allow to find unit cell in Minimum Image Convention, resulting in unexpectedly large arrays.|
|**Example file**| aims/run-1/file000028
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**|array is too big; `arr.size * arr.dtype.itemsize` is larger than the maximum possible size.|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:6|
|**Error class**| Semantic|
|**Comment**| Unphysical geometry does not allow to find unit cell in Minimum Image Convention, resulting in memory errors.|
|**Example file**| aims/run-0/file000008
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:7|
|**Error class**| Semantic|
|**Comment**| Unphysical system can not be used to find unit cell in Minimum Image Convention. Therefore, matid crashes.|
|**Example file**| aims/run-1/file000052
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|DwwGroUpthlSGBt9iVsGOsoF_kIJ|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:8|
|**Error class**| Semantic|
|**Comment**| Parser fails (expectedly) when attempting to divide the number of kpoints by a number of spins that was parsed as 0. However, for the successful runs, this problem does not appear, because the parsing of the program settings fails, thus the default value of the spin channels is chosen, which is 1.|
|**Example file**| aims/run-1/file000060
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|quXZkwi_3tBRaaag_BjEzPc2AiPp|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:9|
|**Error class**| Semantic|
|**Comment**| Another variant of failing to reshape the (arbitrary) eigenvalues. Semantic error.|
|**Example file**| aims/run-1/file000008
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|hfCj4oGLs55vWnCWiGvDzgcuRqH7|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:10|
|**Error class**| Semantic|
|**Comment**| Unphysical unit cell breaks system classification by matid.|
|**Example file**| aims/run-2/file000082
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|HhhIrAyiKk-q2EDKL8ekWUpYLs0J|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:11|
|**Error class**| Semantic|
|**Comment**| Unphysical atomic positions break system normalizer.|
|**Example file**| aims/run-3/file000056
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Op54Up8lxWBrBHUHMym4gvsuXShR|
|**nomad.cli.error**|Singular matrix|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:12|
|**Error class**| Semantic|
|**Comment**| Unphysical system breaks Minimal Image Convention description of unit cell.|
|**Example file**| aims/run-3/file000084
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|-hHp4dzmbfgq5L8JoXyhisxV9jAL|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:13|
|**Error class**| Semantic|
|**Comment**| Unphysical system crashes normalization in MIC convention.|
|**Example file**| aims/run-16/file000024
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|2n04qJKFWHYLrisjLf9jghaXUogz|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:14|
|**Error class**| Semantic|
|**Comment**| Error finding MIC because of unphysical system.|
|**Example file**| aims/run-4/file000008
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|hnU7FBaHMUIs-cXYbp4zgZuYCYSR|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:15|
|**Error class**| Semantic|
|**Comment**| Unphysical system breaks MIC convention description. Potentially interesting due to BLAS library error.|
|**Example file**| aims/run-5/file000060
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|845uR0ZSJ5h5738tdOSyfBVLzq8j|
|**nomad.cli.error**|On entry to DGEMM parameter number 4 had an illegal value|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:16|
|**Error class**| Semantic|
|**Comment**| Error finding periodic dimensions because of unphysical system.|
|**Example file**| aims/run-6/file000011
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|ernpmR8_YzVXVXSas_asOjKytLJt|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:17|
|**Error class**| Semantic|
|**Comment**| Unphysical system breaks MIC determination.|
|**Example file**| aims/run-9/file000054
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|kqWH2wQLrhJySgUOD2nQLGzQk43P|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:18|
|**Error class**| Semantic|
|**Comment**| Unphysical system breaks MIC determination.|
|**Example file**| aims/run-10/file000048
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|0dL3usxUoEtNOcF8oXL24zOxKYcM|
|**nomad.cli.error**|Singular matrix|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:19|
|**Error class**| Semantic|
|**Comment**| Unphysical system breaks determination of MIC. Potentially interesting numpy error.|
|**Example file**| aims/run-11/file000082
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|nxzqQx6YBXZk6pl75DyhnWWj9I_w|
|**nomad.cli.error**|setting an array element with a sequence.|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:20|
|**Error class**| Semantic|
|**Comment**| Error in matid: find_mic|
|**Example file**| aims/run-12/file000087
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Ax34Us_ORApLKN7IHi1PIFeoZZ1P|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:21|
|**Error class**| Semantic|
|**Comment**| Error in matid: find_mic, expected numpy library BLAS error.|
|**Example file**| aims/run-23/file000007
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Ax34Us_ORApLKN7IHi1PIFeoZZ1P|
|**nomad.cli.error**|On entry to DGEMM parameter number 4 had an illegal value|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:22|
|**Error class**| Semantic|
|**Comment**| Most likely an unphysical system, suspected error around np.asarray in matid.geometry.get_neighbour_cells|
|**Example file**| aims/run-24/file000072
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Ax34Us_ORApLKN7IHi1PIFeoZZ1P|
|**nomad.cli.error**|unsupported operand type(s) for *: 'range' and 'float'|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:23|
|**Error class**| Semantic|
|**Comment**| Memory error in matid find_mic|
|**Example file**| aims/run-14/file000022
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|qMTO58yfXPNQnnqP6neALPa8EXrQ|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:24|
|**Error class**| Semantic|
|**Comment**| Error in finding periodic dimensions|
|**Example file**| aims/run-18/file000045
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|h2cL8znAvo-Q4yWPVSNWBZ69OENP|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:25|
|**Error class**| Semantic|
|**Comment**| memory error in matid find_mic|
|**Example file**| aims/run-19/file000038
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|L0caJnXqcryxsjXo9f-LayDiMpVt|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:26|
|**Error class**| Semantic|
|**Comment**| memory error in matid find_mic|
|**Example file**| aims/run-25/file000055
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|845uR0ZSJ5h5738tdOSyfBVLzq8j|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:semantic:27|
|**Error class**| Semantic|
|**Comment**| Unkown error in matid find_mic, suspected error around np.asarray in matid.geometry.get_neighbour_cells|
|**Example file**| aims/run-25/file000066
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|K1jMUp0VICwbP2XJ4ZCoIKXWKVSu|
|**nomad.cli.error**|setting an array element with a sequence.|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:syntactic:0|
|**Error class**| Syntactic|
|**Comment**| The timing information uses a specific different format that requires to use capital letters for scientific notation of floats, e.g. '1E-1'.|
|**Example file**| aims/run-0/file000015
|**Details**| |
|**message**|Error setting value|
|**error_type**|WARNING|
|**nomad.cli.data**|{'quantity': 'time_run_cpu1_start'}|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:syntactic:1|
|**Error class**| Syntactic|
|**Comment**| The timing information uses a specific different format that requires to use capital letters for scientific notation of floats, e.g. '1E-1'.|
|**Example file**| aims/run-0/file000001
|**Details**| |
|**message**|Error setting value|
|**error_type**|WARNING|
|**nomad.cli.data**|{'quantity': 'time_run_wall_start'}|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:syntactic:2|
|**Error class**| Syntactic|
|**Comment**| Random species string breaks regex which determines atomic positions.|
|**Example file**| aims/run-7/file000012
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|1XfjOYpPlGfodWWWINZtgJDW8Hqq|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:0|
|**Error class**| Downstream|
|**Comment**| The timing information uses a specific different format that requires to use capital letters for scientific notation of floats, e.g. '1E-1'. Therefore the regex is broken and wrong values are passed to the metainfo.|
|**Example file**| aims/run-0/file000034
|**Details**| |
|**message**|Error setting run metainfo|
|**error_type**|WARNING|
|**nomad.cli.data**|{'key': 'time_run_wall_start'}|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:1|
|**Error class**| Downstream|
|**Comment**| The timing information uses a specific different format that requires to use capital letters for scientific notation of floats, e.g. '1E-1'. Therefore the regex is broken and wrong values are passed to the metainfo.|
|**Example file**| aims/run-0/file000002
|**Details**| |
|**message**|Error setting run metainfo|
|**error_type**|WARNING|
|**nomad.cli.data**|{'key': 'time_run_cpu1_start'}|
|**nomad.cli.parser**|parsers/fhi-aims|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:2|
|**Error class**| Downstream|
|**Comment**| If the parsing is not successful, the normalizer can not identify a section system, which does not exist because the parser crashed.|
|**Example file**| aims/run-0/file000002
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:3|
|**Error class**| Downstream|
|**Comment**| If the parsing is not successful, the normalizer can not identify a section system, which does not exist because the parser crashed.|
|**Example file**| aims/run-0/file000002
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|OptimadeNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:4|
|**Error class**| Downstream|
|**Comment**| The normalizer skips normalizing if no atomic positions could be parsed.|
|**Example file**| aims/run-7/file000012
|**Details**| |
|**message**|no atom positions, skip further system analysis|
|**error_type**|WARNING|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:5|
|**Error class**| Downstream|
|**Comment**| Sub-sub-package error. SPGLIB (symmetry determination) fails (most likely due to unhysical system).|
|**Example file**| aims/run-16/file000092
|**Details**| |
|**message**|matid symmetry analysis fails with exception|
|**error_type**|ERROR|
|**exception_hash**|9nQpKuw7ROu6jRXeWU7sQeoedTWg|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| aims:downstream:6|
|**Error class**| Downstream|
|**Comment**| Exception is hard failure of spglib.|
|**Example file**| aims/run-0/file000022
|**Details**| |
|**message**|failed to process encyclopedia data due to an unhandlable exception|
|**error_type**|ERROR|
|**nomad.cli.enc_status**|failure|
|**nomad.cli.normalizer**|EncyclopediaNormalizer|
| | |
|**----**|**----**|
| | |

## Errors for code: espresso

| Key | Description |
| :--- | :--- |
|**ID**| espresso:logical:0|
|**Error class**| Logical|
|**Comment**| No subsection to hold x_qe_section_bands_diagonalization. Default fallback section is not defined in metainfo. Syntactic (sign for numbers) mismatch for scf iteration raises logical error.|
|**Example file**| espresso/run-0/file000001
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|AvG5qteoarrjqNZoavltKuoB49Ja|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:logical:1|
|**Error class**| Logical|
|**Comment**| No subsection to hold x_qe_section_bands_diagonalization. Default fallback section is not defined in metainfo. Syntactic (sign for numbers) mismatch for scf iteration raises logical error.|
|**Example file**| espresso/run-0/file000013
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|eCiUa08vtAGFZyCTTT1tlQF6bIhR|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:logical:2|
|**Error class**| Logical|
|**Comment**| Uncaught exception in spglib, most likely due to unphysical system.|
|**Example file**| espresso/run-1/file000045
|**Details**| |
|**additional_exceptions**|["    'Spglib error when finding symmetry dataset.')\n", 'matid.exceptions.CellNormalizationError: Spglib error when finding symmetry dataset.\n']|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:0|
|**Error class**| Semantic|
|**Comment**| File contains a forces section, but the forces are empty.|
|**Example file**| espresso/run-0/file000018
|**Details**| |
|**message**|Error setting value|
|**error_type**|WARNING|
|**nomad.cli.data**|{'quantity': 'forces'}|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:1|
|**Error class**| Semantic|
|**Comment**| Unphysical system description; memory error in matid find_mic|
|**Example file**| espresso/run-0/file000001
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:2|
|**Error class**| Semantic|
|**Comment**| Lattice parameter is set to 0, which leads to a ZeroDivisionError during parsing.|
|**Example file**| espresso/run-0/file000002
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|t986AjaroLIuiNUxFMlQImkKzdk7|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:3|
|**Error class**| Semantic|
|**Comment**| Nullvector as cell vector leads to assertion.|
|**Example file**| espresso/run-0/file000002
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|57YamOvgvaRUgjZNc_PlrnsfHPjH|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:4|
|**Error class**| Semantic|
|**Comment**| Lattice parameter 0 produces ZeroDivisionError.|
|**Example file**| espresso/run-0/file000011
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|d9TcTDKe4Xi95m4WMDqPuJrYzimE|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:5|
|**Error class**| Semantic|
|**Comment**| Atom label replaced by special character leads to deviation between atom positions and labels|
|**Example file**| espresso/run-0/file000054
|**Details**| |
|**message**|len of atom position does not match number of atoms|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:6|
|**Error class**| Semantic|
|**Comment**| Unphysical system produces memory error in matid find_mic|
|**Example file**| espresso/run-0/file000028
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|mcRUPaXQaD9oV5dhmMzZ792nf974|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:7|
|**Error class**| Semantic|
|**Comment**| Unphysical atom positions result in singular matrix in ASE.|
|**Example file**| espresso/run-0/file000032
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Op54Up8lxWBrBHUHMym4gvsuXShR|
|**nomad.cli.error**|Singular matrix|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:8|
|**Error class**| Semantic|
|**Comment**| Unphysical system raises memory error in matid find_mic|
|**Example file**| espresso/run-0/file000037
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|qkMjKLtYkj4WgMn3IIU7mLDT7Y51|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:9|
|**Error class**| Semantic|
|**Comment**| Unphysical system raises memory error in matid find_mic|
|**Example file**| espresso/run-0/file000077
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|2n04qJKFWHYLrisjLf9jghaXUogz|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:10|
|**Error class**| Semantic|
|**Comment**| Volume is set to 0, this warning is shown because the reciprocal cell volume is inverse to the volume and explicitly calculated in the parsing.|
|**Example file**| espresso/run-13/file000059
|**Details**| |
|**additional_exceptions**|['  reciprocal_cell *= (2 * np.pi / volume)\n']|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:11|
|**Error class**| Semantic|
|**Comment**| Memory error in matid find_mic.|
|**Example file**| espresso/run-1/file000077
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|DwwGroUpthlSGBt9iVsGOsoF_kIJ|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:12|
|**Error class**| Semantic|
|**Comment**| Matid find_mic error.|
|**Example file**| espresso/run-9/file000023
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**|array is too big; `arr.size * arr.dtype.itemsize` is larger than the maximum possible size.|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:13|
|**Error class**| Semantic|
|**Comment**| Matid error, most likely integer overflow in numpy|
|**Example file**| espresso/run-10/file000009
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Cy9swkza6WeJ35IQbF-Pd-AsNZZc|
|**nomad.cli.error**|negative dimensions are not allowed|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:14|
|**Error class**| Semantic|
|**Comment**| Matid error in find_mic|
|**Example file**| espresso/run-2/file000010
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|K1jMUp0VICwbP2XJ4ZCoIKXWKVSu|
|**nomad.cli.error**|setting an array element with a sequence.|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:15|
|**Error class**| Semantic|
|**Comment**| Matid failed with memory error in find_mic.|
|**Example file**| espresso/run-7/file000085
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|qMTO58yfXPNQnnqP6neALPa8EXrQ|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:16|
|**Error class**| Semantic|
|**Comment**| Matid error, cell matrix is not inverable, in find_mic.|
|**Example file**| espresso/run-10/file000003
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|0dL3usxUoEtNOcF8oXL24zOxKYcM|
|**nomad.cli.error**|Singular matrix|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:17|
|**Error class**| Semantic|
|**Comment**| Error in matid, suspected around np.asarray in matid.geometry.get_neighbour_cells|
|**Example file**| espresso/run-14/file000086
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|Ax34Us_ORApLKN7IHi1PIFeoZZ1P|
|**nomad.cli.error**|unsupported operand type(s) for *: 'range' and 'float'|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:semantic:18|
|**Error class**| Semantic|
|**Comment**| Memory error in matid find_mic.|
|**Example file**| espresso/run-20/file000031
|**Details**| |
|**message**|matid project system classification failed|
|**error_type**|ERROR|
|**exception_hash**|L0caJnXqcryxsjXo9f-LayDiMpVt|
|**nomad.cli.error**||
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:syntactic:0|
|**Error class**| Syntactic|
|**Comment**| This contains anything that is related to bad formatting or wrong strings (e.g. random or negative numbers) in eigenvalue description.|
|**Example file**| espresso/run-0/file000013
|**Details**| |
|**message**|Error reading eigenvalues.|
|**error_type**|WARNING|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:syntactic:1|
|**Error class**| Syntactic|
|**Comment**| Syntactic error setting the pseudo-potential information. Random strings produce non-processable strings, due to usage of Python str.isalpha().|
|**Example file**| espresso/run-0/file000072
|**Details**| |
|**message**|Error setting value|
|**error_type**|WARNING|
|**nomad.cli.data**|{'quantity': 'atom_species_pp'}|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:syntactic:2|
|**Error class**| Syntactic|
|**Comment**| Occurs when atom positions are empty lists in file -and- random string in atom labels in header. Error could not be traced back to source code.|
|**Example file**| espresso/run-1/file000004
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|ogwg3-AfjwKWeMLdchsxAfaXRx80|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:syntactic:3|
|**Error class**| Syntactic|
|**Comment**| Random string for atom label in pseudo potential was fuzzed and interpreted as integer.|
|**Example file**| espresso/run-26/file000078
|**Details**| |
|**message**|parsing was not successful|
|**error_type**|ERROR|
|**exception_hash**|Q25bjSEMPFtRmRs9_67VWAtQU5bb|
|**nomad.cli.parser**|parsers/quantumespresso|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:downstream:0|
|**Error class**| Downstream|
|**Comment**| The parsing of the atomic system failed.|
|**Example file**| espresso/run-1/file000004
|**Details**| |
|**message**|system has neither atom species nor labels|
|**error_type**|WARNING|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:downstream:1|
|**Error class**| Downstream|
|**Comment**| When the parsing of the system failed, the data for Optimade can not be provided.|
|**Example file**| espresso/run-1/file000004
|**Details**| |
|**message**|could not acquire optimade data|
|**error_type**|WARNING|
|**exception_hash**|sO_OioUn6QJmanbzDfhEnRmCzvSv|
|**nomad.cli.normalizer**|OptimadeNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:downstream:2|
|**Error class**| Downstream|
|**Comment**| If no section system can be created, the system normalizer fails.|
|**Example file**| espresso/run-26/file000078
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|SystemNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:downstream:3|
|**Error class**| Downstream|
|**Comment**| If no section system can be created, the optimade normalizer fails.|
|**Example file**| espresso/run-26/file000078
|**Details**| |
|**message**|no "representative" section system found|
|**error_type**|ERROR|
|**nomad.cli.normalizer**|OptimadeNormalizer|
| | |
|**----**|**----**|
| | |
|**ID**| espresso:downstream:4|
|**Error class**| Downstream|
|**Comment**| Exception is failure of spglib|
|**Example file**| espresso/run-1/file000045
|**Details**| |
|**message**|failed to process encyclopedia data due to an unhandlable exception|
|**error_type**|ERROR|
|**nomad.cli.enc_status**|failure|
|**nomad.cli.normalizer**|EncyclopediaNormalizer|
| | |
|**----**|**----**|
| | |

